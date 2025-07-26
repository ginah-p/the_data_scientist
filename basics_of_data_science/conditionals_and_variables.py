import random

def num_classifier(numbers):

    # Generate a random number between 1 and 100
     numbers = [random.randint(1, 100) for _ in range(15)]

     classifier = {}

    #Checks for even and odd numbers and classifys them
     for num in numbers:
          if num % 2 == 0:
               classifier[num] = "Even"
          else:
               classifier[num] = "Odd"

     even_numbers = list(classifier.values()).count("Even")
     odd_numbers = list(classifier.values()).count("Odd")

     print(classifier)
     print(f"Even : ", even_numbers)
     print(f"Odd : ", odd_numbers)
print(num_classifier(15))
               


    