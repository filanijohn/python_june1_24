class Dog:  #() parenthesis
    # name ='Buddy'
    # color = 'Yellow'
    # height = 10
    # age = 29
    # breed = 'pitbull'
    
# def profile(name, age):
#     print(name, age)
    
    def __init__(self , name, color, height, weight, breed, age,): # init function to defined attributes
        self.name = name
        self.color = color
        self.height = height
        self.weight = weight
        self.breed = breed
        self.age = age
    def __str__(self):
        return self.name
    
    def checkspeed(self):
        if self.breed.casefold() == 'retrieval':
            return f'{self.name} is a {self.breed}, can run atleast 30kmph'
        elif self.breed.casefold() == 'chihuaha':
            return f'{self.name} is a {self.breed}, can run max 15kmph'
        elif self.breed.casefold() == 'yorkshire':
            return f'{self.name} is a {self.breed}, can run max 15kmph'
        elif self.breed.casefold() == 'malinois':
            return f'{self.name} is a {self.breed}, can run max 35kmph'
        elif self.breed.casefold() == 'german sheperd':
            return f'{self.name} is a {self.breed}, can run max 35kmph'
        elif self.breed.casefold() == 'pitbull':
            return f'{self.name} is a {self.breed}, can run max 25kmph'
        else:
            return f'{self.name} speed can not defined'
        
    def aggresiveness(self):
        if self.breed.casefold() == 'retrival':
            return f'{self.name} is a very kind'
        elif self.breed.casefold() == 'chihuaha':
            return f'{self.name} is born to be wicked'
        elif self.breed.casefold() == 'yorkshire':
            return f'{self.name} is friendly'
        elif self.breed.casefold() == 'malinois':
            return f'{self.name} is very aggresive'
        elif self.breed.casefold() == 'german sheperd':
            return f'{self.name} is very aggresive'
        elif self.breed.casefold() == 'pitbull':
            return f'{self.name} is max aggresive'
        else:
            return f'{self.name} aggresiveness can not be checked'
        
    
        


dog1 = Dog(
        name = 'Lassy',
        color = 'brown yellow',
        height  = 1.3,
        weight = 3,
        breed = 'basengi',
        age = 12
    )

dog2 = Dog(
        name = 'Scrophy',
        color = 'light brown',
        height  = 1,
        weight = 3,
        breed = 'basengi',
        age  = 12
    )
dog3 = Dog(
        name = 'Persie',
        color = 'white',
        height  = 2,
        weight = 4,
        breed = 'basengi',
        age  = 7
    )
dog4 = Dog(
        name = 'Jacky',
        color = 'black brown',
        height  = 2.8,
        weight = 5,
        breed = 'basengi',
        age  = 9
    )
print(dog1)
print(dog2)
print(dog3)
print(dog4)
print(dog1.name)
print(dog1.color)
        
