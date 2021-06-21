class FormatFile:

    def get_format(self):
        pass


class FormatFileCSV(FormatFile):

    def get_format(self):
        return ","

class FormatFileXML(FormatFile):

    def get_format(self):
        return "<></>"

class FormatFileJSON(FormatFile):

    def get_format(self):
        return "{}"

class FormatFilePickle(FormatFile):

    def get_format(self):
        return "binary python file"

class Database:
    def connect(self):
        raise NotImplemented

class DatabaseMySQL(Database):
    def connect(self):
        pass

class DatabasePostgres:
    def connect(self):
        pass

