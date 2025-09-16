# Animal Polymorphism Example

class Dog:
    def move(self):
        print("Running 🐕")

class Bird:
    def move(self):
        print("Flying 🐦")

class Fish:
    def move(self):
        print("Swimming 🐟")


# Main program
def main():
    # Create instances of animals
    animals = [Dog(), Bird(), Fish()]

    print("Animal Movements:")
    for animal in animals:
        animal.move()


if __name__ == "__main__":
    main()
