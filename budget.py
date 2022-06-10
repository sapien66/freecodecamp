class Category:

  #seting up the name and ledger
  def __init__(self, name):
    self.name = name
    self.ledger = list()

  # catergory totals string method
  def __str__(self):
    top = (self.name . center(30, "*")) + "\n" # top line with the name of the category and a bunch of stars

    #for each item in the ledger make a line with the item and the price with correct formatting
    line =""
    for item in self.ledger:
      iidp= ("{:.2f}".format(item['amount'])) #make the each amount 2 decimal places
      line += "{:<23}".format(item['description'][0:23]) + "{:>7}".format(iidp[0:7]) + "\n" #add name and price on one line

    total = "Total: " + str(self.get_balance()) #Line showing the total

    breakdown = top + line + total #all lines put together
    return breakdown
    #print(breakdown)

  #method which finds the total withdrawls in a category
  def withdrawls(self):
    total = 0
    for t in self.ledger: #loop through transactoins in the ledger
        amount = t["amount"]
        if amount < 0: # if amount is below 1 (e.g a withdrawl) then it is added to total
            total += amount #all withdrawls in the ledger are added up

    return -total

  #set up the deposit method
  def deposit(self, amount, description = ""):
    """A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise."""
    self.ledger.append({"amount": amount, "description": description}) # add the deposit to the ledger with a decriptoin and amount


  #set up the withdraw method
  def withdraw(self, amount, description = ""):
    """A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise."""
    if self.check_funds(amount) == True: #check whether there is enough funds in the ledger, if there is then make the withdraw
     self.ledger.append({"amount": -amount, "description": description})
     return True #once withdraw is done then return true
    else:
     return False #if there is not enough funds then return false


  #set up the get balance method
  def get_balance(self):
    """A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred."""
    total = 0
    for item in self.ledger: #add up the amount of each of the entries in the ledger adn return the total
      total += item["amount"]
    return total


  #set up transfer method
  def transfer(self, amount, cat):
    """A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise."""
    if self.check_funds(amount) == True: # check if there is enough funds to make the transfer
      self.ledger.append({"amount" : -amount, "description": "Transfer to " + cat.name}) #remove the funds from one category
      cat.ledger.append({"amount" : amount, "description" : "Transfer from " + self.name}) #add funds to the other category
      return True # return true once done
    else:
      return False # if there is not enough funds then return false


  #set up check funds method
  def check_funds(self, amount):
    """A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method."""
    if amount > self.get_balance(): #checks an amount against the total funds in the ledger
      return False #if the amount is greater than the funds then  return false
    else:
      return True # if the funds are greater than or equal to the amount then return true



#seperate function which creates the spending chart
def create_spend_chart(categories):
    allwithdrawls = [c.withdrawls() for c in categories]
    total = sum(allwithdrawls) #total of all withdrawls in all categories
    percentages = [s * 100 / total for s in allwithdrawls] # calculate each categories percentage
    ss = ["Percentage spent by category"] #title
    for i in range(0, 11):
        level = 10 * (10 - i)
        s = '{:>3}| '.format(level)
        for p in percentages:
            if p >= level:
                s += "o  "
            else:
                s += "   "
        ss.append(s)
    padding = " " * 4
    ss.append(padding + "-" * 3 * len(allwithdrawls) + "-")

    #adding correctly formatted category names to the end of the string
    names = [c.name for c in categories]
    n = max(map(len, names)) #find the longest named category
    for i in range(0, n):
        s = padding
        for name in names:
            s += " "
            s += name[i] if len(name) > i else " "
            s += " "


        ss.append(s + " ")

    return "\n".join(ss)
