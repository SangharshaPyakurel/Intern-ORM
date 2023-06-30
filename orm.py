from custom_exception import *
class CSV_Saver:
    def __init__(self): 
        self.filename = self.__class__.__name__.lower()  #instance variables


    #instance method
    def save(self):  #self refers to current objects 
        #instance variables  retrieves the values of current obj and store it in list called values
        values = list(self.__dict__.values())  
        try:
            with open(f'{self.filename}.csv','r') as file:
                data = file.readlines()
        
        except FileNotFoundError:
            with open(f'{self.filename}.csv','w') as file: #create filename
                keys = ''
                for i in self.__dict__.keys():
                    keys+=i+","
                file.writelines(keys[:-1])
            data=[]
        id=str(self.id)
        my_data = [i for i in data if i!="\n"] #filtering out any empty lines("\n")
        print(my_data)
        for i in my_data:
            if id in i:
                raise UniqueIdException("Id must be Unique!")
         #concatenat from values
        string = ""
        # print(values,"##")
        for i in values:
            string+=str(i)
            string+=","
        string=string[:-1]

        with open(f'{self.filename}.csv','a') as file:
            file.writelines(f"\n{string}")
            print("Successfuly saved data!")
    
    #instance method 
    def delete(self):
        with open(f'{self.filename}.csv','r') as file:
            data = file.readlines()
        id = str(self.id)
        num = None
        for i in range(len(data)):
            if id in data[i]:
                num=i
                break
        if num!=None:
            data[num]=""
        else:
            raise CorrectIdException("Enter Correct Id")
        
        with open(f'{self.filename}.csv','w') as file:
            file.writelines(data)
            print("Successfully Deleted!")

    def update(self,*newdata): #*newdata is allow flexiblity  ,splat unpacking accept variable number of  args as a tuple
        with open(f'{self.filename}.csv','r') as file:
            data = file.readlines()
        id = str(newdata[0])
        num = None
        if str(self.id) == id:
            for i in range(len(data)):
                if id in data[i]:
                    print(data[i])
                    num=i
                    break
            if num!=None:
                data[num]=','.join(map(str, newdata))
            else:
                raise CorrectIdException("Enter Correct Id")

            with open(f'{self.filename}.csv','w+') as file:
                file.writelines(data)
                print('Sucessfully Updated!')
        else:
            raise CorrectIdException("Enter Correct Id")

    def get(self):
        # it makes dictionary
        print(self.__dict__) 

    # This function is used to get all objects class method 
    @classmethod
    def get_all(cls):   #cls refers to class  refers to reads the content of CSV file
        objects = []
        try:
            with open(f'{cls.__name__.lower()}.csv','r') as file:
                data = file.readlines()
        except FileNotFoundError:
            raise ConfirmException("Confirm It Before Save!")
        newdata = [i for i in data if i!= "\n"]

        for i in newdata:
            values = i.strip().split(",")
            # creats a new obj of clas unppack value form values slicing used to create copy of values to avoid modyfying
            obj = cls(*values[:]) 
            objects.append(obj)

        object_list = []
        for obj in objects:
            #create tuple to represent the obj name and id
            obj_name = (type(obj).__name__,obj.id) 
            # print(obj_name)
            object_list.append(obj_name)
        return object_list
        
class User(CSV_Saver):
    def __init__(self,id,name,age):
        #super is used for calling parent constructor
        super().__init__() 
        self.id=id
        self.name= name
        self.age = age
    
u1 = User(2,"Sangharsha",21)
u2 = User(3,"Sunil",23)
u2 = User(4,"Sar",22)
u1.save()
u2.save()
u2.update(4,"sarrr",23)
# u2.delete()

class Product(CSV_Saver):
    def __init__(self,id,category,price):
        super().__init__()
        self.id= id
        self.category = category
        self.price = price

p1 = Product(2,"Electronics",200)
p2 = Product(3,"Clothes",200)

p1.save()
p1.update(2,"Laptop",200)
p1.delete()
# p1.delete()
# p2.save()

class Animal(CSV_Saver):
    def __init__(self,id,name,close):
        super().__init__()
        self.id = id
        self.name = name
        self.close = close 
a1 = Animal(1,"Cow","milk")
a2 = Animal(2,"Crow","milk")
a1.save()
a2.save()
a1.update(2,"LAptop",200)

class Season(CSV_Saver):
    def __init__(self, id, name, app):
        super().__init__()
        self.id = id
        self.name = name
        self.app = app

r1 = Season(1, "Winter", "Hot")
r2 = Season(2, "Winter", "Cold")
r1.save()
r2.save()
all_seasons = Season.get_all()
print(all_seasons)
