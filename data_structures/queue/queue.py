class Queue:
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        return str(self.queue)

    def put(self, data):
        self.queue.append(data)
    
    def get(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            raise IndexError

if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.put(i)
        print(q)
    for i in range(10):
        print(q.get())
    
    q.rotation(3)
    print(q)
