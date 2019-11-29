
class Utils:
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

# l1=[1,2,3]
# l2=[4,5,6]
# l3=[l1,l2]

# h4=[7,8,9]

# k5=[l3,h4]

# x=[0,0,0]
# y=[[x]+k5[0],k5[1]]
# print(y[0][0][0])