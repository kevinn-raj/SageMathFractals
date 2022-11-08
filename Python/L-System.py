import numpy as np
from matplotlib import pyplot as plt

class MyTurtle():
    """
    
    """

    
    def __init__(self, angle = 0, position = np.array((0,0), dtype=float)):
        self.__angle = angle
        self.__position = position
    
    def left(self, a):
        self.__angle += a
        
    def right(self, a):
        self.__angle -= a
        
    def forward(self, l):
        d = l * np.array((np.cos(self.__angle), np.sin(self.__angle)))
        self.__position += d
        
    def back(self, l):
        d = - l * np.array((np.cos(self.__angle), np.sin(self.__angle)))
        self.__position += d
    
    def get_angle(self):
        return self.__angle
    
    def get_position(self):
        return self.__position
    
def grow_2(axiom, variables, rules, angle, distance, iterations = 5):
    result = axiom

    for i in range(iterations):
        tmp = []
        for r in result:
            if r == variables[0]:
                tmp.append(r.upper().replace(variables[0], rules[0]))
            elif r == variables[1]:
                tmp.append(r.upper().replace(variables[1], rules[1]))
            else:
                tmp.append(r)
        result = "".join(tmp)

    t = MyTurtle()
    d = distance
    a = angle

    path = [t.get_position()]

    for r in result:
        if r.upper() == variables[0]:
            t.forward(d)
            p = t.get_position()
            path.append(p)
        elif r.upper() == variables[1]:
            t.forward(d)
            p = t.get_position()
            path.append(p)
        elif r.upper() == "+":
            t.left(a)
        elif r.upper() == "-":
            t.right(a)

    return path

angle = 120
angle = angle * np.pi/180
axiom = "F+G+G"
rules = "F+G-F-G+F" , "GG"

iterations = 2

path3d = []
paths = grow_2(axiom = str(axiom), variables=("F", "G"), rules = rules,
                angle = angle, distance = 1, iterations = iterations)

# plt.plot(paths[:,0], paths[:, 1])
print(paths)