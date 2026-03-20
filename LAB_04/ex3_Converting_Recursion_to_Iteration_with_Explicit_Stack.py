from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Comment:
    content: str
    replies: List["Comment"] = field(default_factory=list)


def flatten_recursive(comment: Comment) -> List[Comment]:
    result = []

    def depth_first(current: Comment) -> None:
        if current is None:
            return

        result.append(current)

        for reply in current.replies:
            depth_first(reply)

    depth_first(comment)
    return result



def flatten_iterative(comment: Comment) -> List[Comment]:
    result = []

    if comment is None:
        return result

    STATE_START = 0
    STATE_REPLIES_DONE = 1

    stack: List[Tuple[Comment, int]] = []
    stack.append((comment, STATE_START))

    while stack:
        current, state = stack.pop()

        if state == STATE_START:
            result.append(current)

            stack.append((current, STATE_REPLIES_DONE))

            for i in range(len(current.replies) - 1, -1, -1):
                stack.append((current.replies[i], STATE_START))

        elif state == STATE_REPLIES_DONE:
            # replies already processed
            pass

    return result





def count_comments_tail(comment: Comment, accumulator: int) -> int:
    if comment is None:
        return accumulator

    accumulator += 1

    for reply in comment.replies:
        accumulator = count_comments_tail(reply, accumulator)

    return accumulator





def count_comments_loop(comment: Comment) -> int:
    if comment is None:
        return 0

    count = 0
    stack: List[Comment] = [comment]

    while stack:
        current = stack.pop()
        count += 1

        for reply in current.replies:
            stack.append(reply)

    return count




################################ test ################################

print("\ntest 0")

subreply1 = Comment("SubReply1")
reply1 = Comment("Reply1", [subreply1])
reply2 = Comment("Reply2")
comment = Comment("Comment1", [reply1, reply2])

flat_recursive = flatten_recursive(comment)
flat_iterative = flatten_iterative(comment)

print("Recursive flatten:", [c.content for c in flat_recursive])
print("Iterative flatten:", [c.content for c in flat_iterative])

print("Count_comments_tail):", count_comments_tail(comment, 0))
print("Count_comments_loop:", count_comments_loop(comment))




################################### test 1 ##############################

print("\ntest 1")

comment = None

flat_recursive = flatten_recursive(comment)
flat_iterative = flatten_iterative(comment)

print("Recursive flatten:", [c.content for c in flat_recursive])
print("Iterative flatten:", [c.content for c in flat_iterative])

print("Count_comments_tail:", count_comments_tail(comment, 0))
print("Count_comments_loop:", count_comments_loop(comment))


################################### test 2 ##############################

print("\nTest 2")

comment = Comment("Comment1")

flat_recursive = flatten_recursive(comment)
flat_iterative = flatten_iterative(comment)

print("Recursive flatten:", [c.content for c in flat_recursive])
print("Iterative flatten:", [c.content for c in flat_iterative])

print("Count_comments_tail:", count_comments_tail(comment, 0))
print("Count_comments_loop:", count_comments_loop(comment))


################################### test 3 ##############################

print("\nTest 3")

comment = Comment("Comment1", [])

flat_recursive = flatten_recursive(comment)
flat_iterative = flatten_iterative(comment)

print("Recursive flatten:", [c.content for c in flat_recursive])
print("Iterative flatten:", [c.content for c in flat_iterative])

print("Count_comments_tail:", count_comments_tail(comment, 0))
print("Count_comments_loop:", count_comments_loop(comment))



################################### test 4 ##############################

print("\nTest 4")

subreply2 = Comment("SubReply2")
subreply1 = Comment("SubReply1", [subreply2])
reply1 = Comment("Reply1", [subreply1])
comment = Comment("Comment1", [reply1])

flat_recursive = flatten_recursive(comment)
flat_iterative = flatten_iterative(comment)

print("Recursive flatten:", [c.content for c in flat_recursive])
print("Iterative flatten:", [c.content for c in flat_iterative])

print("Count_comments_tail:", count_comments_tail(comment, 0))
print("Count_comments_loop:", count_comments_loop(comment))



################################### test 5 ##############################

print("\nTest 5")

reply1 = Comment("Reply1")
reply2 = Comment("Reply2")
reply3 = Comment("Reply3")
reply4 = Comment("Reply4")
comment = Comment("Comment1", [reply1, reply2, reply3, reply4])

flat_recursive = flatten_recursive(comment)
flat_iterative = flatten_iterative(comment)

print("Recursive flatten:", [c.content for c in flat_recursive])
print("Iterative flatten:", [c.content for c in flat_iterative])

print("Count_comments_tail:", count_comments_tail(comment, 0))
print("Count_comments_loop:", count_comments_loop(comment))



################################### test 6 ##############################

print("\nTest 6")

subreply1 = Comment("SubReply1")
subreply2 = Comment("SubReply2")
subreply3 = Comment("SubReply3")

reply1 = Comment("Reply1", [subreply1, subreply2])
reply2 = Comment("Reply2", [subreply3])

comment = Comment("Comment1", [reply1, reply2])

flat_recursive = flatten_recursive(comment)
flat_iterative = flatten_iterative(comment)

print("Recursive flatten:", [c.content for c in flat_recursive])
print("Iterative flatten:", [c.content for c in flat_iterative])

print("Count_comments_tail:", count_comments_tail(comment, 0))
print("Count_comments_loop:", count_comments_loop(comment))






