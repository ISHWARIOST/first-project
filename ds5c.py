from collections import deque
def reverse_queue_recursive(queue):
    if not queue:
        return
    item=queue.popleft()
    reverse_queue_recursive(queue)
    queue.append(item)
q=deque([10,20,30,40,50])
print("Original queue:", list(q))
reverse_queue_recursive(q)
print("reversed queue:", list(q))
