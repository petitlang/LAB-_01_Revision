from datetime import datetime


class StoryNode:
    def __init__(self, story_id: int, user_id: int, content_preview: str,
                 timestamp: datetime, views: int = 0):
        self.story_id = story_id
        self.user_id = user_id
        self.content_preview = content_preview
        self.timestamp = timestamp
        self.views = views
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    # Function add_story(node)
    def add_story(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.current = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.size = self.size + 1

    # Function remove_story(story_id)
    def remove_story(self, story_id):
        temp = self.head

        while temp is not None:

            if temp.story_id == story_id:

                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next is not None:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev

                if self.current == temp:
                    self.current = temp.next

                self.size = self.size - 1
                return True

            temp = temp.next

        return False

    # Function move_forward()
    def move_forward(self):
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next

        return self.current

    # Function move_backward()
    def move_backward(self):
        if self.current is not None and self.current.prev is not None:
            self.current = self.current.prev

        return self.current

    # Function jump_to(story_id)
    def jump_to(self, story_id):
        temp = self.head

        while temp is not None:
            if temp.story_id == story_id:
                self.current = temp
                return temp

            temp = temp.next

        return None

    # Function insert_after(current_id, new_story)
    def insert_after(self, current_id, new_story):
        temp = self.head

        while temp is not None:
            if temp.story_id == current_id:
                new_story.next = temp.next
                new_story.prev = temp

                if temp.next is not None:
                    temp.next.prev = new_story
                else:
                    self.tail = new_story

                temp.next = new_story
                self.size = self.size + 1
                return True

            temp = temp.next

        return False

    # Function display_around_current(k)
    def display_around_current(self, k):
        if self.current is None:
            return None

        temp = self.current
        count = 0

        while temp.prev is not None and count < k:
            temp = temp.prev
            count = count + 1

        count = 0
        result = []

        while temp is not None and count < 2 * k + 1:
            result.append(
                (
                    temp.story_id,
                    temp.user_id,
                    temp.content_preview,
                    temp.timestamp,
                    temp.views
                )
            )
            print(temp.story_id, temp.user_id, temp.content_preview, temp.timestamp, temp.views)
            temp = temp.next
            count = count + 1

        return result





if __name__ == "__main__":



############################   test 0   ###############################

    print("\ncase 0: normal list")


    story_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)
    s4 = StoryNode(4, 104, "Story4", datetime.now(), 5)


    story_list.add_story(s1)
    story_list.add_story(s2)
    story_list.add_story(s3)

    print("after add story:")
    temp = story_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", story_list.current.content_preview)

    story_list.move_forward()
    print("after moveforward, current story:", story_list.current.content_preview)

    story_list.move_backward()
    print("after movebackward, current story:", story_list.current.content_preview)

    story_list.jump_to(3)
    print("after jump to story3, current story:", story_list.current.content_preview)

    story_list.insert_after(2, s4)
    print("after insert story 4 after story 2:")
    temp = story_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("display around current k=1:")
    story_list.display_around_current(1)

    story_list.remove_story(2)
    print("after remove story2:")
    temp = story_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next



############################   test 1   ###############################


    
    print("\ncase 1: empty list")

    empty_list = DoublyLinkedList()

    print("current story:", empty_list.current)

    empty_list.move_forward()
    print("\nafter moveforward, current story:", empty_list.current)



    empty_list = DoublyLinkedList()
    empty_list.move_backward()
    print("\nafter movebackward, current story:", empty_list.current)


    empty_list = DoublyLinkedList()
    empty_list.jump_to(3)
    print("\nafter jump to story3, current story:", empty_list.current)


    empty_list = DoublyLinkedList()
    s1 = StoryNode(10, 110, "EmptyInsert", datetime.now(), 0)
    empty_list.insert_after(2, s1)
    print("\nafter insert after on empty list, current story:", empty_list.current)

    temp = empty_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next



    empty_list = DoublyLinkedList()
    print("\ndisplay around current k=1:")
    result = empty_list.display_around_current(1)
    print("result:", result)



    empty_list = DoublyLinkedList()
    empty_list.remove_story(2)
    print("\nafter remove story2, current story:", empty_list.current)

    temp = empty_list.head
    while temp is not None:
        print("\nstory:", temp.story_id, "-", temp.content_preview)
        temp = temp.next


    empty_list = DoublyLinkedList()
    s1 = StoryNode(10, 110, "Story1", datetime.now(), 0)
    empty_list.add_story(s1)
    print("\nafter add story, current story:", empty_list.current.content_preview)

    temp = empty_list.head
    while temp is not None:
        print("\nstory:", temp.story_id, "-", temp.content_preview)
        temp = temp.next



############################   test 2   ###############################

    print("\ncase 2: single story")


    single_list = DoublyLinkedList()
    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    single_list.add_story(s1)

    print("current story:", single_list.current.content_preview)


    single_list.move_forward()
    print("after moveforward, current story:", single_list.current.content_preview)



    single_list = DoublyLinkedList()
    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    single_list.add_story(s1)

    single_list.move_backward()
    print("after movebackward, current story:", single_list.current.content_preview)



    single_list = DoublyLinkedList()
    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    single_list.add_story(s1)

    single_list.jump_to(1)
    print("after jump to story1, current story:", single_list.current.content_preview)



    single_list = DoublyLinkedList()
    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    single_list.add_story(s1)

    single_list.insert_after(1, s2)
    print("after insert story2 after story1:")
    temp = single_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next



    single_list = DoublyLinkedList()
    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    single_list.add_story(s1)

    print("display around current k=1:")
    single_list.display_around_current(1)
    



    single_list = DoublyLinkedList()
    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    single_list.add_story(s1)

    single_list.remove_story(1)
    print("after remove story1:")
    temp = single_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", single_list.current)






############################   test 3   ###############################
    print("\ncase 3: remove non-existing story")


    test_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)

    test_list.add_story(s1)
    test_list.add_story(s2)
    test_list.add_story(s3)

    print("before remove story:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview)


    test_list.remove_story(99)   

    print("after remove story99:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview)




############################   test 4   ###############################

    print("\ncase 4: remove head/tail/middle story")

    test_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)

    test_list.add_story(s1)
    test_list.add_story(s2)
    test_list.add_story(s3)

    print("before remove story:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview)

    test_list.remove_story(1)

    print("after remove head story (story1):")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview if test_list.current is not None else None)



    test_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)

    test_list.add_story(s1)
    test_list.add_story(s2)
    test_list.add_story(s3)


    test_list.remove_story(3)

    print("after remove tail story (story3):")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview if test_list.current is not None else None)



    test_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)

    test_list.add_story(s1)
    test_list.add_story(s2)
    test_list.add_story(s3)

    test_list.remove_story(2)

    print("after remove middle story (story2):")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview if test_list.current is not None else None)




############################   test 5   ###############################

    print("\ncase 5: remove current story")

    test_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)

    test_list.add_story(s1)
    test_list.add_story(s2)
    test_list.add_story(s3)


    test_list.jump_to(2)

    print("before remove story:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview)


    test_list.remove_story(2)

    print("after remove current story:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview if test_list.current is not None else None)







############################   test 6   ###############################


    print("\ncase 6: move forward when current is tail")

    test_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)

    test_list.add_story(s1)
    test_list.add_story(s2)
    test_list.add_story(s3)

    test_list.jump_to(3)

    print("before moveforward:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview)

    test_list.move_forward()

    print("after moveforward:")
    print("current story:", test_list.current.content_preview)







############################   test 7   ###############################

    print("\ncase 7: move backward when current is head")

    test_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)

    test_list.add_story(s1)
    test_list.add_story(s2)
    test_list.add_story(s3)

    print("before movebackward:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview)

    test_list.move_backward()

    print("after movebackward:")
    print("current story:", test_list.current.content_preview)











############################   test 8   ###############################

    print("\ncase 8: jump to non-existing story")

    test_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)

    test_list.add_story(s1)
    test_list.add_story(s2)
    test_list.add_story(s3)

    print("before jump to non-existing story:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview)

    test_list.jump_to(99)

    print("after jump to story99:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview)








############################   test 9   ###############################
    print("\ncase 9: display around current with k greater than list size")

    test_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)

    test_list.add_story(s1)
    test_list.add_story(s2)
    test_list.add_story(s3)

    test_list.jump_to(2)

    print("before display:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview)
    test_list.display_around_current(10)












############################   test 10   ###############################
    print("\ncase 10: display around current with k=1")

    test_list = DoublyLinkedList()

    s1 = StoryNode(1, 101, "Story1", datetime.now(), 0)
    s2 = StoryNode(2, 102, "Story2", datetime.now(), 2)
    s3 = StoryNode(3, 103, "Story3", datetime.now(), 1)

    test_list.add_story(s1)
    test_list.add_story(s2)
    test_list.add_story(s3)

    test_list.jump_to(2)

    print("before display:")
    temp = test_list.head
    while temp is not None:
        print("story:", temp.story_id, "-", temp.content_preview)
        temp = temp.next

    print("current story:", test_list.current.content_preview)

    print("display around current k=1:")
    test_list.display_around_current(1)



