public class Exercise2FeedProcessing {

    /* =========================
       Part A - Activity Stack
       ========================= */

    static class ActivityNode {
        String activity;
        ActivityNode next;

        ActivityNode(String activity) {
            this.activity = activity;
            this.next = null;
        }
    }

    static class ActivityStack {
        private ActivityNode top;
        private int count;

        public ActivityStack() {
            this.top = null;
            this.count = 0;
        }

        public void push(String activity) {
            ActivityNode newNode = new ActivityNode(activity);
            newNode.next = top;
            top = newNode;
            count++;
        }

        public String pop() {
            if (top == null) {
                return null;
            }

            String activity = top.activity;
            top = top.next;
            count--;
            return activity;
        }

        public String peek() {
            if (top == null) {
                return null;
            }
            return top.activity;
        }

        public boolean isEmpty() {
            return top == null;
        }

        public int size() {
            return count;
        }

        public void displayRecent(int n) {
            ActivityNode current = top;
            int i = 0;

            while (current != null && i < n) {
                System.out.println(current.activity);
                current = current.next;
                i++;
            }
        }

        public void undoLast(ActivityStack undoStack) {
            String activity = pop();
            if (activity != null) {
                undoStack.push(activity);
            }
        }

        public void displayAll() {
            ActivityNode current = top;
            while (current != null) {
                System.out.println(current.activity);
                current = current.next;
            }
        }
    }

    /* =========================
       Part B - Notification Queue
       ========================= */

    static class NotificationNode {
        String notification;
        NotificationNode next;

        NotificationNode(String notification) {
            this.notification = notification;
            this.next = null;
        }
    }

    static class NotificationQueue {
        private NotificationNode front;
        private NotificationNode rear;
        private int count;

        public NotificationQueue() {
            this.front = null;
            this.rear = null;
            this.count = 0;
        }

        public void enqueue(String notification) {
            NotificationNode newNode = new NotificationNode(notification);

            if (rear == null) {
                front = newNode;
                rear = newNode;
            } else {
                rear.next = newNode;
                rear = newNode;
            }

            count++;
        }

        public String dequeue() {
            if (front == null) {
                return null;
            }

            String notification = front.notification;
            front = front.next;

            if (front == null) {
                rear = null;
            }

            count--;
            return notification;
        }

        public String front() {
            if (front == null) {
                return null;
            }
            return front.notification;
        }

        public boolean isEmpty() {
            return front == null;
        }

        public int size() {
            return count;
        }

        public void displayPending() {
            NotificationNode current = front;
            while (current != null) {
                System.out.println(current.notification);
                current = current.next;
            }
        }

        public void priorityEnqueue(String notification) {
            NotificationNode newNode = new NotificationNode(notification);
            newNode.next = front;
            front = newNode;

            if (rear == null) {
                rear = newNode;
            }

            count++;
        }
    }

    /* =========================
       Part C - Feed Processor
       ========================= */

    static class FeedProcessor {
        private ActivityStack recentActivities;
        private NotificationQueue notificationQueue;
        private NotificationQueue processedLog;

        public FeedProcessor() {
            this.recentActivities = new ActivityStack();
            this.notificationQueue = new NotificationQueue();
            this.processedLog = new NotificationQueue();
        }

        public ActivityStack getRecentActivities() {
            return recentActivities;
        }

        public NotificationQueue getNotificationQueue() {
            return notificationQueue;
        }

        public NotificationQueue getProcessedLog() {
            return processedLog;
        }

        public void processIncoming() {
            String notification = notificationQueue.dequeue();
            if (notification != null) {
                recentActivities.push(notification);
            }
        }

        public void batchProcess(int k) {
            int i = 0;
            while (i < k && !notificationQueue.isEmpty()) {
                String notification = notificationQueue.dequeue();
                recentActivities.push(notification);
                i++;
            }
        }

        public void clearHistory() {
            while (!recentActivities.isEmpty()) {
                String activity = recentActivities.pop();
                processedLog.enqueue(activity);
            }
        }

        public void getStats() {
            System.out.println("Recent activities size: " + recentActivities.size());
            System.out.println("Notification queue size: " + notificationQueue.size());
            System.out.println("Processed log size: " + processedLog.size());
        }
    }

    /* =========================
       Main Test
       ========================= */

    public static void main(String[] args) {
        ActivityStack undoStack = new ActivityStack();
        FeedProcessor feed = new FeedProcessor();

        // Part A test
        feed.getRecentActivities().push("Liked video");
        feed.getRecentActivities().push("Commented on post");
        feed.getRecentActivities().push("Shared photo");

        System.out.println("Recent activities:");
        feed.getRecentActivities().displayAll();

        System.out.println("\nUndo last activity:");
        feed.getRecentActivities().undoLast(undoStack);

        System.out.println("Recent activities after undo:");
        feed.getRecentActivities().displayAll();

        System.out.println("Undo stack:");
        undoStack.displayAll();

        // Part B test
        feed.getNotificationQueue().enqueue("New follower");
        feed.getNotificationQueue().enqueue("New like");
        feed.getNotificationQueue().enqueue("New comment");

        System.out.println("\nNotification queue:");
        feed.getNotificationQueue().displayPending();

        System.out.println("\nPriority enqueue:");
        feed.getNotificationQueue().priorityEnqueue("Urgent alert");
        feed.getNotificationQueue().displayPending();

        // Part C test
        System.out.println("\nProcess one incoming notification:");
        feed.processIncoming();

        System.out.println("Recent activities:");
        feed.getRecentActivities().displayAll();

        System.out.println("Notification queue:");
        feed.getNotificationQueue().displayPending();

        System.out.println("\nBatch process 2 notifications:");
        feed.batchProcess(2);

        System.out.println("Recent activities:");
        feed.getRecentActivities().displayAll();

        System.out.println("Notification queue:");
        feed.getNotificationQueue().displayPending();

        System.out.println("\nClear history:");
        feed.clearHistory();

        System.out.println("Processed log:");
        feed.getProcessedLog().displayPending();

        System.out.println();
        feed.getStats();

        System.out.println("\n===== Edge Case Tests =====");

        /* 1. Pop from empty stack */
        ActivityStack emptyStack = new ActivityStack();
        System.out.println("Pop from empty stack: " + emptyStack.pop()); // expected: null

        /* 2. Peek on empty stack */
        System.out.println("Peek on empty stack: " + emptyStack.peek()); // expected: null

        /* 3. Push one activity into empty stack */
        emptyStack.push("like");
        System.out.println("After pushing one activity:");
        System.out.println("Top activity: " + emptyStack.peek()); // expected: like
        System.out.println("Stack size: " + emptyStack.size());   // expected: 1

        /* 4. Undo on empty stack */
        ActivityStack emptyMainStack = new ActivityStack();
        ActivityStack emptyUndoStack = new ActivityStack();
        emptyMainStack.undoLast(emptyUndoStack);
        System.out.println("Undo on empty stack:");
        System.out.println("Main stack size: " + emptyMainStack.size()); // expected: 0
        System.out.println("Undo stack size: " + emptyUndoStack.size()); // expected: 0

        /* 5. Dequeue from empty queue */
        NotificationQueue emptyQueue = new NotificationQueue();
        System.out.println("Dequeue from empty queue: " + emptyQueue.dequeue()); // expected: null

        /* 6. Enqueue one notification into empty queue */
        emptyQueue.enqueue("New follower");
        System.out.println("After enqueue one notification:");
        System.out.println("Front notification: " + emptyQueue.front()); // expected: New follower
        System.out.println("Queue size: " + emptyQueue.size());          // expected: 1

        /* 7. Dequeue the only notification */
        System.out.println("Dequeued notification: " + emptyQueue.dequeue()); // expected: New follower
        System.out.println("Queue is empty: " + emptyQueue.isEmpty());        // expected: true

        /* 8. Priority enqueue into non-empty queue */
        NotificationQueue testQueue = new NotificationQueue();
        testQueue.enqueue("New comment");
        testQueue.enqueue("New like");
        testQueue.priorityEnqueue("Urgent alert");
        System.out.println("Priority enqueue into non-empty queue:");
        testQueue.displayPending();
// expected order:
// Urgent alert
// New comment
// New like

        /* 9. ProcessIncoming with empty notification queue */
        FeedProcessor emptyFeed = new FeedProcessor();
        emptyFeed.processIncoming();
        System.out.println("ProcessIncoming with empty notification queue:");
        emptyFeed.getStats();
// expected:
// Recent activities size: 0
// Notification queue size: 0
// Processed log size: 0

        /* 10. BatchProcess with k larger than queue size */
        FeedProcessor batchFeed = new FeedProcessor();
        batchFeed.getNotificationQueue().enqueue("N1");
        batchFeed.getNotificationQueue().enqueue("N2");
        batchFeed.batchProcess(5);
        System.out.println("BatchProcess with k larger than queue size:");
        System.out.println("Recent activities:");
        batchFeed.getRecentActivities().displayAll();
// expected: N2 then N1
        System.out.println("Notification queue size: " + batchFeed.getNotificationQueue().size()); // expected: 0

        /* 11. ClearHistory with empty activity stack */
        FeedProcessor clearEmptyFeed = new FeedProcessor();
        clearEmptyFeed.clearHistory();
        System.out.println("ClearHistory with empty activity stack:");
        clearEmptyFeed.getStats();
// expected:
// Recent activities size: 0
// Notification queue size: 0
// Processed log size: 0

        /* 12. GetStats on empty structures */
        FeedProcessor statsFeed = new FeedProcessor();
        System.out.println("GetStats on empty structures:");
        statsFeed.getStats();
// expected:
// Recent activities size: 0
// Notification queue size: 0
// Processed log size: 0
    }
}