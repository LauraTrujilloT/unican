import numpy as np

class Shape:
    """
    A class used to represent a geometrical shape.

    Attributes
    ----------
    **kwargs (dictionary)

    Methods
    --------
    Operators:
    __add__ () add each parameter of object. *class should have items method
        and new method implemented.

    Comparators:
    __gt__  () Greater than
    __ge__  () Greater than or equal
    __lt__ () less than
    __le__ () less or equal
    __eq__ () equal
    __ne__ () not equal

    """
    #Initializing
    def __init__(self, **kwargs):
        """
        Initializating Shape

        Parameters:
        ----------
        **kwargs variable number of keyword arguments dictionary
        """
        for attname, attvalue in kwargs.items():
            if attvalue < 0:
                raise ValueError("All parameters should be positive")
            else:
                setattr(self, attname, attvalue)

    #Methods

    #Operators
    def __add__(self, other):
        """
        "+" Operator returns the sum between two shapes in this module.
        Class should have item-method and new-method implemented.
        """
        its = self.items()
        other_its = other.items()
        newlst = [];
        if self.__class__ != other.__class__:
            raise TypeError("Geometrical shapes should be of same type")
        else:
            for i in range(len(its)):
                newlst.append(its[i] + other_its[i])
        return self.new(newlst)


    def __mul__(self, other):
        raise NotImplementedError()

    def __sub__(self, other):
        raise NotImplementedError()

    def __truediv__(self, other):
        raise NotImplementedError()

    def __pow__(self, other):
        raise NotImplementedError()

    # Comparators
    def __gt__(self, other):
        """
        Returns bool:
        (True) if area first element is greater than second element area
        """
        return (self.area > other.area)

    def __ge__(self, other):
        """
        Returns bool:
        (True) if area first element is greater or equal
        than second element area
        """
        return (self.area >= other.area)

    def __lt__(self, other):
        """
        Returns bool:
        (True) if area of first element is less than second element area
        """
        return (self.area < other.area)

    def __le__(self, other):
        """
        Returns bool:
        (True) if area of first element is less or equal than second element area
        """
        return (self.area <= other.area)

    def __eq__(self, other):
        """
        Returns bool:
        (True) if area of first element is equal to second element area
        """
        return (self.area == other.area)

    def __ne__(self, other):
        """
        Returns bool:
        (True) if area of first element is not equal to second element area
        """
        return (self.area != other.area)

class Triangle(Shape):
    """
    A child-class of Shape used to represent triangles

    Attributes
    ---------
    height (float) height of triangle
    base   (float) base of triangle

    Methods
    -------
    items (list) returns list of parameters.
    new (Triangle) returns a new triangle
    """

    # Initializing
    def __init__(self, height=1.0, base=1.0):
        super().__init__(height=height, base=base)
        self.area = 0.5 * base * height
        self.perimeter = base + height + (base ** 2 + height ** 2) ** (0.5)

    #Methods
    def __str__(self):
        """
        Formatted string of a triangle
        """
        return "Object Triangle" + "  base: {} & height: {}".format(self.base, self.height)

    def __repr__(self):
        """
        Returns (string) with information about class Triangle.
        """
        return "Triangle({}, {})".format(self.height, self.base)

    def items(self):
        """
        Returns (list) of parameters of the object
        """
        return list([self.height, self.base])

    def new(self, params):
        """
        Creates a new Triangle with a list of parameters.
        """
        return Triangle(params[0],params[1])

    #Operators
    def __sub__(self, other):
        """
        Returns a new Triangle with substracted parameters of the first and second
        triangles.
        """
        params = list([np.abs(self.height - other.height), np.abs(self.base - other.base)])
        return self.new(params)

    def __mul__(self, other):
        """
        Returns a new Triangle with parameters being the multiplication
        of the first triangle params with second triangle params.
        """
        params = list([self.height * other.height, self.base * other.base])
        return self.new(params)

    def __truediv__(self, other):
        """
        Returns a new Triangle with the division of each parameters
        """
        params = list([self.height / other.height, self.base / other.base])
        return self.new(params)

class Circle(Shape):
    """
    A child-class of Shape used to represent circles

    Attributes
    ---------
    radius (float) radius of circle

    Methods
    -------
    items (list) returns list of parameters.
    new (Circle) returns a new cirlce
    """
    # Initializing
    def __init__(self, radius=1.0):
        super().__init__(radius=radius)
        self.area =  np.pi * (radius ** 2)
        self.perimeter = 2 * np.pi * radius

    #Methods
    def __str__(self):
        """
        Formatted string of a Circle
        """
        return "Object Circle" + "  radius: {} ".format(self.radius)

    def __repr__(self):
        """
        Returns (string) with information about class Circle.
        """
        return "Circle({})".format(self.radius)

    def items(self):
        """
        Returns (list) of parameters of the object
        """
        return list([self.radius])

    def new(self, params):
        """
        Creates a new circle with a list of parameters.
        """
        return Circle(params[0])

    #Operators
    def __sub__(self, other):
        """
        Returns a new Circle with substracted parameters of the first and second
        triangles.
        """
        params = list([np.abs(self.radius - other.radius)])
        return self.new(params)

    def __mul__(self, other):
        """
        Returns a new Circle with parameters being the multiplication
        of the first triangle params with second triangle params.
        """
        params = list([self.radius * other.radius])
        return self.new(params)

    def __truediv__(self, other):
        """
        Returns a new Circle  with the division of each parameters
        """
        params = list([self.radius / other.radius])
        return self.new(params)

class Rectangle(Shape):
    """
    A child-class of Shape used to represent Rectangle

    Attributes
    ---------
    length (float) length of rectangle
    width   (float) width of rectangle

    Methods
    -------
    items (list) returns list of parameters.
    new (Rectangle) returns a new Rectangle
    """

    # Initializing
    def __init__(self, length=1.0, width=1.0):
        super().__init__(length=length, width=width)
        self.area = length * width
        self.perimeter = 2 * length + 2 * width

    #Methods
    def __str__(self):
        """
        Formatted string of a Rectangle
        """
        return "Object Rectangle" + "  length: {} & width: {}".format(self.length, self.width)

    def __repr__(self):
        """
        Returns (string) with information about class Rectangle.
        """
        return "Rectangle({}, {})".format(self.length, self.width)

    def items(self):
        """
        Returns (list) of parameters of the object
        """
        return list([self.length, self.width])

    def new(self, params):
        """
        Creates a new Rectangle with a list of parameters.
        """
        return Triangle(params[0],params[1])

    #Operators
    def __sub__(self, other):
        """
        Returns a new Rectangle with substracted parameters of the first and second
        rectangles.
        """
        params = list([np.abs(self.length - other.length), np.abs(self.width - other.width)])
        return self.new(params)

    def __mul__(self, other):
        """
        Returns a new Rectangle with parameters being the multiplication
        of the first rectangle params with second triangle params.
        """
        params = list([self.length * other.length, self.width * other.width])
        return self.new(params)

    def __truediv__(self, other):
        """
        Returns a new Rectangle with the division of each parameters
        """
        params = list([self.length / other.length, self.width / other.width])
        return self.new(params)
