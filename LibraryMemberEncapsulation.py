class LibraryMember:
    def __init__(self, member_id, name, membership_type):
        self.member_id = member_id              # Public attribute
        self.name = name                        # Public attribute
        self.__membership_type = membership_type  # Private attribute

    def get_membership_type(self):
        return self.__membership_type

    def set_membership_type(self, membership_type):
        if membership_type in ["Regular", "Premium"]:
            self.__membership_type = membership_type
        else:
            print("Invalid membership type!")

    def display_member_details(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Membership Type: {self.get_membership_type()}")

# Creating a LibraryMember object
member = LibraryMember("LM1001", "Alice Johnson", "Regular")

# Displaying member details
member.display_member_details()
# Output:
# Member ID: LM1001
# Name: Alice Johnson
# Membership Type: Regular

# Changing membership type
member.set_membership_type("Premium")
member.display_member_details()
# Output:
# Member ID: LM1001
# Name: Alice Johnson
# Membership Type: Premium
