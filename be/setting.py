class Setting():
    def getconstrString(self):
         with open("constr.txt") as k:
            return str(k.read())