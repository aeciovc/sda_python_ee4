import threading
import time

def find_value(iter, value):
    for item in iter:
        time.sleep(3)
        if item == value:
            return item

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self) -> None:
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


t1 = ThreadWithReturnValue(find_value, args=(range(10), 8))
t1.start()

result = t1.join()

print("Done, the result is ", result)





"""
class ThreadForHttpRequests(threading.Thread):

    def __request(self, url):
        pass

    def __init__(self, url):
        self.url = url

    def run(self) -> None:
        self.result = self.__request(self.url)


t1 = ThreadForHttpRequests("http://google.com")
t1.start()
result = t1.join()
"""