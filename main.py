class User:
    def __init__(self,id,name):
        self._id = id
        self._name = name
    def vivoduser(self):
        return self._id, self._name

    def addu(self, id, name):
        self._id = id
        self._name = name

    def deleteu(self):
        self._id = None
        self._name = None

class Admin(User):
    def __init__(self, id, name, status):
        super().__init__(id, name)
        self.__status = status

    def add(self, id, name, status):
        self._id = id
        self._name = name
        self.__status = status

    def vivod(self):
        return self._id,self._name,self.__status


    def delete(self):
        self._id = None
        self._name = None
        self.__status = None

user=User(None,None)
admin=Admin(None,None,None)

while True:
    scale = input("доступ:\n1 админ\n2 юзер \nАвторизуйтесь: ")
    if scale == "1":
        print("доступ админ\n1 - добавить\n2 - удалить\n3 - список\nввод: ")
        x = input()
        if x == "1":
            id = input("введите id: ")
            name = input("введите имя: ")
            status = input("введите статус: ")
            admin.add(id,name,status)
            user.addu(id,name)
            print(admin.vivod())
        if x == "2":
            admin.delete()
            user.deleteu()
            print(admin.vivod())
        if x == "3":
            print(admin.vivod())
    if scale == "2":
        print("доступ юзер\n1 - список\nввод: ")
        x = input()
        if x == "1":
            print(user.vivoduser())















































