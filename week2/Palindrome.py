class Pal:
    def palindrome(self, string):
        if string == string[::-1]:
            return "is a palindrome"
        else:
            return "is not a palindrome"


print("no capital letters please")
string = input("Type a word: ")

obj = Pal()
f = obj.palindrome(string)

print(string, f)
