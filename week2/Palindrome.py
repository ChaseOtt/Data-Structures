class Pal:
    def palindrome(self, string):
        if string == string[::-1]:
            return "is a palindrome"
        else:
            return "is not a palindrome"


x = 1

while x == 1:
    print("no capital letters please")
    string = input("Type a word: ")

    obj = Pal()
    f = obj.palindrome(string)

    print(string, f)
    x = int(input("Try again? 1 = yes, any other number = no:  "))
