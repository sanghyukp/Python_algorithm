
def put(item):
    queue.append(item)

def get():
    return queue.pop(0)

if __name__ == "__main__":
    queue = []
    put(1)
    put(2)
    put(3)
    put(4)
    put(5)
    print("current queue status")
    print(queue)
    
    while queue:
        print("POP : {}".format(get()))
