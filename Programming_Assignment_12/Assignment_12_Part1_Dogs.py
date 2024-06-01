#author == Srivaishnavi
#Network Programming Assignment_12 Part-2

def main():
    class Dog:
        species = "Canis familiaris"

        def __init__(self, name, age ,breed):
            self.name = name
            self.age = age
            self.breed = breed
        
        def __str__(self):
            return f"{self.name} is {self.age} years old and belongs to {self.breed} breed"

        def speak(self, sound):
            return f"{self.name} barks as {sound}"
        
        def strength(self, power):
            return f"{self.name} strenghth is  {power} PSI"

    class Husky(Dog):
         def speak(self, sound="Hi"):
             return(f"{self.name} barks as {sound}")
        
    class Retriever(Dog):
        pass

    class poodle(Dog):
         def strength(self, power="200 Pound-force per Square inch"):
             return(f"{self.name} strengh is {power}")
    
    
    joe = Dog("joe", 4,"Husky Dog")
    print(joe)
    joe = Husky("jack",5,"Husky Dog") #Calling speak method from Husky class 
    print(f"{joe.speak()}\n")
    
    jimmy = Retriever("jimmy",6,"Retriever")
    print(jimmy)
    jimmy = Dog("jimmy",7,"Retriever")
    print(jimmy.speak("boww"))                             #calling speak method from parent class
    print("\n")
    
    jack = Dog("jack",7,"poodle")
    print(jack)
    jack = poodle("jack",7,"poodle")           #calling power method from poodle class
    print(f"{jack.strength()}\n")


if __name__ == "__main__":
     main()