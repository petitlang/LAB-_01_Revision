from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class CommentNode:
    comment_id: int
    user_id: str
    content: str
    timestamp: date
    likes: int
    replies: List["CommentNode"] = field(default_factory=list)


def display_thread(comment: CommentNode, level: int) -> None:
    indent = ""

    for i in range(0, level + 1):
        indent = indent + "  "

    print(f"{indent}Comment {comment.comment_id} ({comment.user_id}) {comment.content}")

    for reply in comment.replies:
        display_thread(reply, level + 1)


def count_total_comments(comment: CommentNode) -> int:
    total = 1

    for reply in comment.replies:
        total = total + count_total_comments(reply)

    return total


def total_likes(comment: CommentNode) -> int:
    total = comment.likes

    for reply in comment.replies:
        total = total + total_likes(reply)

    return total


def find_deepest_reply(comment: CommentNode) -> int:
    depth = 0
    max_depth = 0

    for reply in comment.replies:
        depth = find_deepest_reply(reply)
        max_depth = max(depth, max_depth)

    return max_depth + 1


def search_by_user(user_id: str, comment: CommentNode) -> List[CommentNode]:
    result: List[CommentNode] = []
    sub_result: List[CommentNode] = []

    if comment.user_id == user_id:
        result.append(comment)

    for reply in comment.replies:
        sub_result = search_by_user(user_id, reply)
        for item in sub_result:
            result.append(item)

    return result


def contains_keyword(keyword: str, comment: CommentNode) -> bool:
    if keyword in comment.content:
        return True

    for reply in comment.replies:
        if contains_keyword(keyword, reply):
            return True

    return False


def delete_comment(comment_id: int, thread: Optional[CommentNode]) -> Optional[CommentNode]:
    if thread is None:
        return None

    if thread.comment_id == comment_id:
        return None

    new_replies: List[CommentNode] = []

    for reply in thread.replies:
        updated_reply = delete_comment(comment_id, reply)
        if updated_reply is not None:
            new_replies.append(updated_reply)

    thread.replies = new_replies
    return thread

if __name__ == "__main__":
    print("========== Test Set for Edge Cases ==========\n")
  
    # Test 1: Single comment, no replies
    print("Test 1: Single comment, no replies")
    single = CommentNode(
        comment_id=1,
        user_id="Alice",
        content="Only one comment",
        timestamp=date(2026, 3, 17),
        likes=5
    )

    display_thread(single, 0)
    print("Total comments:", count_total_comments(single))
    print("Total likes:", total_likes(single))
    print("Deepest depth:", find_deepest_reply(single))
    print("Contains keyword 'one':", contains_keyword("one", single))
    print("Search by user 'Alice':", [c.comment_id for c in search_by_user("Alice", single)])
    print()

    # Test 2: Deeply nested thread
    print("Test 2: Deeply nested thread")
    root_deep = CommentNode(10, "UserA", "Root", date(2026, 3, 17), 1)
    c2 = CommentNode(11, "UserB", "Reply level 1", date(2026, 3, 17), 2)
    c3 = CommentNode(12, "UserC", "Reply level 2", date(2026, 3, 17), 3)
    c4 = CommentNode(13, "UserD", "Reply level 3", date(2026, 3, 17), 4)

    root_deep.replies.append(c2)
    c2.replies.append(c3)
    c3.replies.append(c4)

    display_thread(root_deep, 0)
    print("Total comments:", count_total_comments(root_deep))
    print("Total likes:", total_likes(root_deep))
    print("Deepest depth:", find_deepest_reply(root_deep))
    print()

    # Test 3: Multiple replies at same level
    print("Test 3: Multiple replies at same level")
    root_multi = CommentNode(20, "Alice", "Main comment", date(2026, 3, 17), 10)
    r1 = CommentNode(21, "Bob", "First reply", date(2026, 3, 17), 2)
    r2 = CommentNode(22, "Charlie", "Second reply", date(2026, 3, 17), 3)
    r3 = CommentNode(23, "David", "Third reply", date(2026, 3, 17), 4)

    root_multi.replies.extend([r1, r2, r3])

    display_thread(root_multi, 0)
    print("Total comments:", count_total_comments(root_multi))
    print("Total likes:", total_likes(root_multi))
    print("Deepest depth:", find_deepest_reply(root_multi))
    print()

    # Test 4: Search user not found
    print("Test 4: Search user not found")
    result = search_by_user("UnknownUser", root_multi)
    print("Search result:", [c.comment_id for c in result])
    print()
  
    # Test 5: Keyword not found
    print("Test 5: Keyword not found")
    print("Contains keyword 'pizza':", contains_keyword("pizza", root_multi))
    print()

    # Test 6: Delete a leaf comment
    print("Test 6: Delete a leaf comment")
    root_delete_leaf = CommentNode(30, "Alice", "Root comment", date(2026, 3, 17), 5)
    leaf1 = CommentNode(31, "Bob", "Leaf 1", date(2026, 3, 17), 1)
    leaf2 = CommentNode(32, "Charlie", "Leaf 2", date(2026, 3, 17), 2)

    root_delete_leaf.replies.extend([leaf1, leaf2])

    print("Before deletion:")
    display_thread(root_delete_leaf, 0)

    root_delete_leaf = delete_comment(32, root_delete_leaf)

    print("After deleting comment 32:")
    if root_delete_leaf is not None:
        display_thread(root_delete_leaf, 0)
    print()

    # Test 7: Delete a comment with cascade deletion 
    print("Test 7: Delete a comment with cascade deletion")
    root_cascade = CommentNode(40, "Alice", "Root", date(2026, 3, 17), 1)
    child1 = CommentNode(41, "Bob", "Child 1", date(2026, 3, 17), 2)
    child2 = CommentNode(42, "Charlie", "Child 2", date(2026, 3, 17), 3)
    grandchild = CommentNode(43, "David", "Grandchild", date(2026, 3, 17), 4)

    root_cascade.replies.append(child1)
    root_cascade.replies.append(child2)
    child1.replies.append(grandchild)

    print("Before deletion:")
    display_thread(root_cascade, 0)

    root_cascade = delete_comment(41, root_cascade)

    print("After deleting comment 41 (and its replies):")
    if root_cascade is not None:
        display_thread(root_cascade, 0)
    print()

    # Test 8: Delete the root comment  
    print("Test 8: Delete the root comment")
    root_delete_root = CommentNode(50, "Alice", "Root to delete", date(2026, 3, 17), 5)
    child = CommentNode(51, "Bob", "Child comment", date(2026, 3, 17), 2)
    root_delete_root.replies.append(child)

    print("Before deletion:")
    display_thread(root_delete_root, 0)

    root_delete_root = delete_comment(50, root_delete_root)

    print("After deleting root comment:")
    print(root_delete_root)
    print()

    # Test 9: Empty thread input for delete_comment
    print("Test 9: Empty thread input")
    empty_thread = None
    empty_thread = delete_comment(999, empty_thread)
    print("Result:", empty_thread)
    print()

    print("========== End of Edge Case Tests ==========")