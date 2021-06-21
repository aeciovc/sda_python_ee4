import threading

def find_value(iter, value):
    for item in iter:
        if item == value:
            return item


t1 = threading.Thread(target=find_value, args=(range(5), 3))

t1.start()

result = t1.join()

print("Done with result ", result)