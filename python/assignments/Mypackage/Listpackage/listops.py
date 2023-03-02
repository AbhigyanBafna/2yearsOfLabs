
cmpFlag = False

def compare(l1, l2):
        if(len(l1) != len(l2)):
            print("Var Length")
        else:
            for i in l1:
                for j in l2:
                    if(i < j):
                        cmpFlag = True
                    else:
                        cmpFlag = False
            print(cmpFlag)
    
def merge(l1, l2):
        for i in l2:
            l1.append(i)
        print(l1)