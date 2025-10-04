import queue

q = queue.Queue()
numbers = [10, 20, 30, 40, 50, 60, 70]

for number in numbers:
    q.put(number)


print(q.get())
print(q.get())
print(q.get())

# LIFO QUEUE
q = queue.LifoQueue()
numberd = [10, 20, 30, 40, 50, 60, 70]
for number in numberd:
    q.put(number)
print(q.get())


# priority queue
q = queue.PriorityQueue()
q.put((2, "Hello World"))
q.put((1, True))
q.put((10, False))

while not q.empty():
    print(q.get()[1])
