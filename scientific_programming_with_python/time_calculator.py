def add_time(start, duration, weekday = False):

  #index set up with the days of the week and a corresponding weekday number
  weekdayindex = { "monday" : 0 , "tuesday" : 1 , "wednesday" : 2 , "thursday" : 3 , "friday" : 4 , "saturday" : 5 , "sunday" : 6 , }

  #array of weekdays (formatted correctly for use when showing the new weekday)
  weekdayarray = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  #Split the start time in into hour, minute and am/pm variables
  starttuple = start.partition(":")
  minutetuple = starttuple[2].partition(" ")
  starthour = starttuple[0]
  startminute = minutetuple[0]
  ampm = minutetuple[2]

  #Assign a number to whether it is AM or PM to track this (odd is AM , even is PM)
  ampmnum=""
  if ampm == "AM":
    ampmnum=1
  if ampm == "PM":
    ampmnum=2

  #Split the duration into hour and minute variables
  durationtuple = duration.partition(":")
  durationhour = durationtuple[0]
  durationminute = durationtuple[2]

  #Calculate the new hour and minute values before converted
  newminute = int(startminute) + int(durationminute)
  newhour = int(starthour) + int(durationhour)

  ampmflip=0
  dayspast=0

  #if minutes is over an hour then add one to the hour
  if (newminute >= 60):
    newhour += 1
    newminute -= 60
  if (newhour >= 12): #if the hour is over 12 then find remainder hours and the times it flipped from am to pm
    t, r = divmod(newhour,12)
    newhour = r
    ampmflip = t
    ampmnum = ampmnum + ampmflip #track whether it is currently am or pm

    #if the ampm number is even and started in the PM do this to calculate days past
    if (ampmnum % 2) == 0 and ampm == "PM":
      ampm = "PM"
      dayspast, re = divmod(ampmnum,2)
    #if the ampm number is even and started in the AM do the same but minus 1 form days past as the first one doesnt count as a change of day
    elif (ampmnum % 2) == 0 and ampm == "AM":
      ampm = "PM"
      dayspast, re = divmod(ampmnum,2)
      dayspast = dayspast - 1
    #if the ampm number is odd then do this
    else:
      ampm = "AM"
      dayspast, re = divmod(ampmnum-1,2)

  #Add a zero to the front of newminutes if it is only 1 character long
  newminute = str(newminute).zfill(2)

  #if the hour is 0 then make it a 12 to match clock formatting
  if newhour == 0:
    newhour = 12

  #basic final time value put together here
  finaltime = str(newhour) + ":" + str(newminute) + " " + str(ampm)

  #If the weekday paramter is used then do this
  if weekday:
    weekday = weekday.lower() #format the weekday parameter to make sure it is lower case
    index = int((weekdayindex[weekday]) + dayspast) % 7 #find weekday index, add this to the days past, and use modulo to ensure it is within seven
    newday = weekdayarray[index] #Use previously calculated index with the weekday array to find the new weekday
    finaltime += ", " + str(newday) #add this weekday to the basic final time string


  if dayspast == 1: #if the days past is 1 then add the 'next day' part to the string
    finaltime += " (next day)"
  elif dayspast > 1: #if the day past is more than one then add the number of days past to the string
    finaltime += " (" + str(dayspast) + " days later)"

  return finaltime
  
