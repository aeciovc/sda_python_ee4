from contextlib import contextmanager


@contextmanager
def file_manager(name, mode):
    f = open(name, mode)     # __enter__
    yield f
    f.close()                # __exit__


with file_manager("test.txt", 'w') as f:
    f.write("Test")