class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__ (self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width (self, width):
    self.width = width

  def set_height (self, height):
    self.height = height

  def get_area (self):
    area = self.width * self.height
    return area

  def get_perimeter (self):
    perimeter = ((2 * self.width) + (2 * self.height))
    return perimeter

  def get_diagonal (self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture (self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      string=""
      picture=""
      for w in range(self.width):
        string += "*"
      for h in range(self.height):
        picture += string + "\n"
    return picture

  def get_amount_inside (self, shape):
    wtimes, rw = divmod(self.width , shape.width)
    htimes, rh = divmod(self.height , shape.height)
    if wtimes >= 1 and htimes >= 1:
      return wtimes * htimes
    else:
      return 0

class Square(Rectangle):

  def __init__ (self, side):
    self.width = side
    self.height = side


  def __str__ (self):
    return f'Square(side={self.width})'

  def set_side (self, side):
    self.height = side
    self.width = side
