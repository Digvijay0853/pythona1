# class Old_age_Phones:
#
#     def calling(self):
#         print('Old_age_Phones is used to call')
#
# class Smart_phones(Old_age_Phones):
#
#     def calling(self):
#         print('Smart_phones is used to call')
#         super().calling()
# obj = Smart_phones()
# obj.calling()
class Parent:

    def __init__(self):
        print('in parent class constructor')

class Child(Parent):
    def __init__(self):
        super().__init__()
        print('in Child class Constructor')
obj = Child()  #__init__()
