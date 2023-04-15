
class Entry:
    def __init__(self, id, head, body, data):
        self.__id=id
        self.__head=head
        self.__body=body
        self.__data=data
    
    def set_id(self, id):
        self.__id = id

    def set_head(self, head):
        self.__head = head


    def set_body(self, body):
        self.__body = body

    def set_data(self, data):
        self.__data = data

    def get_id(self):
        return self.__id

    def get_head(self):
        return self.__head

    def get_body(self):
        return self.__body

    def get_data(self):
        return self.__data
    
    def get_all(self):
        return f"ID: {self.__id}\nЗаголовок: {self.__head}\nТело заметки:\n{self.__body}\nДата: {self.__data}"

    def get_allf(self):
        return f"{self.__id};{self.__head};{self.__body};{self.__data}\n"
