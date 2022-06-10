import copy
import random
# Consider using the modules imported above.

class Hat:

  #Initialise the object with variables being the key word arguments
  def __init__ (self, **kwargs):
    self.contents = []
    for key, value in kwargs.items(): #for every key and value in the items
      for i in range(value):
        self.contents.append(key) #add the key name to a string for every 1 of its value


  #draw method which accepts the name and number of balls to draw
  def draw (self, num):
    drawn = []
    if num > len(self.contents):
      return self.contents #if the num of balls to draw is greater than the number of balls then return all balls
    else:
      for i in range(num): #loop for the amount of balls drawn
        number = random.randrange(len(self.contents)) #pick a random number from 1 to the number of balls in the hat
        drawn.append(self.contents.pop(number)) #use the random number as index to pick one of the balls from the hat. Remove this ball and add it to a new string
    return drawn

#seperate experiment function
def experiment (hat, expected_balls, num_balls_drawn, num_experiments):
  m=0
  for i in range(num_experiments): #for the number of experiments do this
    expectedball_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat) #Create deep copies of hat and expected balls
    colours_gotten = hat_copy.draw(num_balls_drawn) #draw from hat_copy
    for colour in colours_gotten: #cycle through colours drawn
      if colour in expectedball_copy:
        expectedball_copy[colour] -=1 #if the colour in drawn balls matches expected balls then minus one form drawn ball value
    if all( value <= 0 for value in expectedball_copy.values()):
      m += 1 #if all values are 0 or below then the experiment was successful, therfore add 1 to the number of successes
  probability = m / num_experiments #calculate probability
  return probability
