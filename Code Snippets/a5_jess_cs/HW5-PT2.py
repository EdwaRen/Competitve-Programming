
class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:

    def __init__(self, p1, p2, color):
        self.p1 = p1
        self.p2 = p2
        self.color = color

    def get_bottom_left(self):
        return self.p1

    def get_top_right(self):
        return self.p2

    def get_color(self):
        return self.color

    def reset_color(self, color):
        self.color = color

    def get_perimeter(self):
        x1, y1 = self.p1.get()
        x2, y2 = self.p2.get()

        l = x2-x1
        b = y2-y1
        return 2*(l+b)

    def get_area(self):
        x1, y1 = self.p1.get()
        x2, y2 = self.p2.get()

        l = x2-x1
        b = y2-y1
        return l*b

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def intersects(self, rect):
        return not (self.p2.x < rect.p1.x or self.p1.x > rect.p2.x or self.p2.y < rect.p1.y or self.p1.y > rect.p2.y)

        # if (self.p2.x < rect.p1.x or rect.p2.x < self.p1.x):
        #     return False
    
        # if (self.p2.y < rect.p1.y or rect.p2.y < self.p1.y):
        #     return False
        # return True

    def contains(self, x, y):
        if((self.p1.x<=x) and (self.p2.x>=x)):
            return True
        if((self.p1.y<=y) and (self.p2.y>=y)):
            return True
        return False

    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2 and self.color == other.color

    def __repr__(self):
        return "Rectangle("+repr(self.p1)+","+repr(self.p2)+",'" + self.color + "')"

    def __str__(self):
        return 'I am a '+self.color+' rectangle with bottom left corner at ('+str(self.p1.x)+','+ str(self.p1.y)+') and top right corner at ('+str(self.p2.x)+','+ str(self.p2.y)+')'


class Canvas:

    def __init__(self, c=[]):
        self.c = c

    def add_one_rectangle(self, rect):
        self.c.append(rect)

    def count_same_color(self, color):
        num = 0
        for r in self.c:
            if r.get_color() == color:
                num+=1
        return num

    def total_perimeter(self):
        perimeter = 0
        for r in self.c:
            perimeter += r.get_perimeter()
        return perimeter

    def min_enclosing_rectangle(self):
        min_x = 100000
        max_x = -100000
        min_y = 100000
        max_y = -100000

        for r in self.c:
            if min_x>r.p1.x:
                min_x = r.p1.x
        
            if max_x<r.p2.x:
                max_x = r.p2.x

            if min_y>r.p1.y:
                min_y = r.p1.y

            if max_y<r.p2.y:
                max_y = r.p2.y

            rect = Rectangle(Point(min_x, min_y), Point(max_x, max_y), "red")
        return repr(rect)

    def common_point(self):
        for r1 in self.c:
            for r2 in self.c:
                if not r1.intersects(r2):
                    print(repr(r1), repr(r2))
                    return False
        return True

    def __len__(self):
        return len(self.c)

    def __str__(self):
        str = "Canvas("
        for r in self.c:
            str += repr(r) + ","
            str = str[:-1]
            str += ")"
        return str


r1=Rectangle(Point(), Point(1,1), "red")
print(r1)
print(r1.get_color())
print(r1.get_bottom_left())
print(r1.get_top_right())
r1.reset_color("blue")
print(r1.get_color())
print(r1)
r1.move(2,3)
print(r1)

r2=eval(repr(r1))
print(r2)
print(r1 is r2)
print(r1==r2)

r3=Rectangle(Point(), Point(2,1), "red")
print(r3.get_perimeter())

r4=Rectangle(Point(1,1), Point(2,2.5), "blue")
print(r4.get_area())

r5=Rectangle(Point(1,1), Point(2,2.5), "blue")
print(r4==r5)
print(r4 is r5)

r=Rectangle(Point(1,1), Point(2,5), "blue")
print(r.contains(1.5,1))
print(r.contains(2,2))
print(r.contains(0,0))

r1=Rectangle(Point(1,1), Point(2,2), "blue")
r2=Rectangle(Point(2,2.5), Point(3,3), "blue")
r3=Rectangle(Point(1.5,0),Point(1.7,3),"red")
print(r3)
print(r1.intersects(r2))
print(r2.intersects(r3))
print(r1.intersects(r3))
print(r2.intersects(r3))

c=Canvas()
print(len(c.c))

r1=Rectangle(Point(1,1), Point(2,2), "blue")
r2=Rectangle(Point(2,2.5), Point(3,3), "blue")
r3=Rectangle(Point(1.5,0),Point(1.7,3),"red")
c.add_one_rectangle(r1)
c.add_one_rectangle(r2)
c.add_one_rectangle(r3)
c.add_one_rectangle(Rectangle(Point(0,0),Point(100,100),"orange") )
print(c)
print(len(c))
print(c.count_same_color("blue"))
print(c.count_same_color("red"))
print(c.count_same_color("purple"))

c=Canvas([])
print(c.c)
print("canvas leng", len(c.c))
r1=Rectangle(Point(1,1), Point(2,2), "blue")
r2=Rectangle(Point(1.5,1.5), Point(4,4), "blue")
r3=Rectangle(Point(-2,-2), Point(2,1.5), "blue")
r4=Rectangle(Point(0,-100), Point(1.5,100), "yellow")
c.add_one_rectangle(r1)
c.add_one_rectangle(r2)
c.add_one_rectangle(r3)
c.add_one_rectangle(r4)
print(len(c))
print(c.common_point())

c=Canvas()
print(len(c))
r1=Rectangle(Point(-2,-2), Point(-1,2), "blue")
r2=Rectangle(Point(-2,-2), Point(2,-1), "blue")
r3=Rectangle(Point(1,-2), Point(2,2), "blue")
r4=Rectangle(Point(-2,1), Point(2,2), "blue")
c.add_one_rectangle(r1)
c.add_one_rectangle(r2)
c.add_one_rectangle(r3)
c.add_one_rectangle(r4)
print(len(c))
print(c.common_point())
