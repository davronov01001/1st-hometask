# #dunder methods
# class Rect:
#     # __slots__=["width","height"]
    
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

    
#     def __setattr__(self, __name:str, __value:int)->None:
#         if __name in ("width","heght"):
#             if isinstance(__value,int):
#                 self.__dict__[__name]=__value
#             else:
#                 raise TypeError(f"Cannot set {__name} to {__value}")
#         else:
#              self.__dict__[__name]=__value
#     def __getattr__(self,__name:str) ->any:
#         print ("getattribute")
#         return False
#     def info(self):
#         return f'Rect object width:{self.width}, height:{self.height}'
# rectangle = Rect(width = 19,height = 13)
# # rectangle.color = "red"
# print(rectangle.d)

#dunder methods
class Rect:
    # __slots__=["width","height"]
    
    def __init__(self,width,height):
        self.width = width
        self.height = height

    
    def __setattr__(self, __name:str, __value:int)->None:
        if __name in ("width","heght"):
            if isinstance(__value,int):
                self.__dict__[__name]=__value
            else:
                raise TypeError(f"Cannot set {__name} to {__value}")
        else:
             self.__dict__[__name]=__value
    def __getattr__(self,__name:str) ->any:
        print ("getattribute")
        return False
    def __getattribute_(self,__name:str)->any:
        if __name in ("width"):
            PermissionError: "xatolik"
        return object.__getattribute(self,__name)
    def info(self):
        return f'Rect object width:{self.width}, height:{self.height}'
rectangle = Rect(width = 19,height = 13)
rectangle.color = "red"
print(rectangle.colorq)






# ....fff

"""  uz"""
