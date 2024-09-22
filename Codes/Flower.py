#Ally Magika 09/20/2024

#This program will represent a class of objects, mainly beautiful flowers
#This will contain my comments about each individual code and add an additional flower to the list
#They will be highlighted with my own comments to have "#*" in front of them


class Flower:  # This class represents a flower.
    def __init__(self, name):  # Initialize the flower with its name.
        self.name = name  # Set the name of the flower. # ! this is known as an attribute.

    def grow(self):  # Method to simulate the flower growing.
        print("The " + self.name + " is growing.")  # Print a message indicating the flower is growing. # ! this is known as a method.

    def bloom(self):  # Method to simulate the flower blooming.
        print("The " + self.name + " is blooming.")  # Print a message indicating the flower is blooming. # ! this is also known as a method.

# Main function to create flower objects and demonstrate their behavior.
def main():  # Entry point of the program.
    flower1 = Flower("Rose")  # Create a flower named Rose.
    flower1.grow()  # Simulate the Rose growing.
    flower1.bloom()  # Simulate the Rose blooming.

    flower2 = Flower("Daisy")  # Create a flower named Daisy.
    flower2.grow()  # Simulate the Daisy growing.
    flower2.bloom()  # Simulate the Daisy blooming.

    flower3 = Flower("Lily of the Valley")  #* Create a flower named Lily of the Valley.
    flower3.grow()  #* Simulate the Lily of the Valley growing.
    flower3.bloom()  #* Simulate the Lily of the Valley blooming.

# Execute the main function if the script is run directly.
if __name__ == "__main__":
    main()  # Call the main function.
