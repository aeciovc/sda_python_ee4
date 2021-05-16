
class FileText:

    def __init__(self, file_path):

        if file_path is None or file_path == '':
            raise ValueError

        self.path = file_path

    def read(self):
        with open(self.path) as f:
            lines = f.readlines()
            return lines
