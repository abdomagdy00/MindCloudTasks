import collections

class Phone:
    """
    A class representing a basic phone with contact and call functionalities.
    """
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        """
        Adds a new contact to the phone.
        """
        self.contacts[name] = number
        print(f"Contact '{name}' added with number {number}.")

    def remove_contact(self, name):
        """
        Removes a contact from the phone.
        """
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' removed.")
        else:
            print(f"Contact '{name}' not found.")

    def make_call(self, name):
        """
        Makes a call to a contact if they exist.
        """
        if name in self.contacts:
            print(f"Calling {name}...")
        else:
            print(f"Contact '{name}' not found. Cannot make a call.")

class Camera:
    """
    A class representing a camera with photo-taking functionality.
    """
    def take_pic(self):
        """
        Takes a picture.
        """
        print("The picture was taken successfully.")

class Smartphone(Phone, Camera):
    """
    A class representing a smartphone that inherits from both Phone and Camera.
    """
    def __init__(self):
        # Call the constructors of the parent classes
        Phone.__init__(self)
        Camera.__init__(self)
        print("Smartphone is ready!")

# --- Example of usage ---
if __name__ == "__main__":
    my_phone = Smartphone()

    # Use methods from the Phone class
    my_phone.add_contact("Alice", "123-456-7890")
    my_phone.add_contact("Bob", "987-654-3210")
    my_phone.make_call("Alice")
    my_phone.make_call("Charlie")

    # Use methods from the Camera class
    my_phone.take_pic()

    # Remove a contact
    my_phone.remove_contact("Alice")
    my_phone.make_call("Alice")

