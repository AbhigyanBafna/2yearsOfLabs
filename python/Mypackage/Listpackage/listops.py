
cmpFlag = False

def compare(list1, list2):
        if(len(list1) != len(list2)):
            print("Var Length");
        else:
            for i in range(len(list1)):
                    if(list1[i] < list2[i]):
                        cmpFlag = True
                    else:
                        cmpFlag = False
            print(cmpFlag)
    
def merge(l1, l2):
        for i in l2:
            l1.append(i)
        print(l1)
