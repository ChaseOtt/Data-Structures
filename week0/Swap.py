def Swap():
    def yah(self, ah):
        print(self, ah)
        if self < ah:
            return self, ah
        else:
            x = self
            self = ah
            ah = x
            return self, ah

    a, b = yah(int(input("Big number: ")), int(input("Small Num: ")))
    print(a, b)


