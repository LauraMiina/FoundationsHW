#Laura Kukkonen
#11/5/2023
#Homework 2

#How old the user is

#If someone says they were born in the future, ask them for their year of birth again. Assume they'll do it right the second time.
while True:
        year_of_birth = int(input("Please enter your year of birth: "))
        if year_of_birth <= 2023:
            print ("You are", 2023 - year_of_birth, "years old.")
            break
        if (year_of_birth > 2023):
            pass
        print("This year is in the future.")
        continue

#Using heartbeat rate of 80 per minute for human, 33 for whale and 160 for rabbit
#In that time, how many times the user's heart has beaten.
heart_beat = (2023 - year_of_birth)*365*24*60*80
print("Your heart has beaten about", heart_beat, "times during your lifetime.")

#In that time, how many times a blue whale's heart has beaten.
whale = (2023 - year_of_birth)*365*24*60*33
print("In the same amount of time a blue whale's heart has beaten", whale, "times.")

#In that time, how many times a rabbit's heart has beaten. If the answer to rabbit heartbeats is more than a billion, say "XXX billion" instead of the very long raw number
rabbit_beat = ((2023 - year_of_birth)*365*24*60*160)/1000000000
print("A rabbit's heart has beaten", rabbit_beat, "billion times.")

#There are several ways to calculate and format/display numbers in Python – string addition, f-strings, 
#commas, etc etc etc. Redo one of the above questions above 
#with another technique and briefly explain the pros and cons of each approach.
whale_beat = (2023 - year_of_birth)*365*24*60*33
print("In the same amount of time a blue whale's heart has beaten", whale, "times.")
#I guess with this second option I can just copy paste the print sentence and change the values and variables. In the option above I have some
#variation in the sentences.


#We calculate how much older or younger the user is than me
if year_of_birth < 1989:
    print("You are", 1989 - year_of_birth, "years older than me.")
elif year_of_birth > 1989:
    print("You are", ((1989 - year_of_birth) * (-1)), "years younger than me.")
else:
    print("We are the same age.")

#Let's test if the birth year is even or odd    
if (year_of_birth % 2) == 0:
    print("You were born in an even year.")
else:
    print ("Your year of birth is odd.") 

#How many times there has been a president from the Democratic Party in 
#office since they were born (1980 onward, and each president only counts once)
if year_of_birth >= 1980 and year_of_birth <= 1981:
    print("There have been four Democratic Party presidents in office since you were born.")
if year_of_birth >= 1982 and year_of_birth <= 2008:
    print("There have been three Democratic Party presidents in office since you were born.")
if year_of_birth >= 2009 and year_of_birth <= 2020:
    print("There have been two Democratic Party presidents in office since you were born.")
if year_of_birth >= 2021 and year_of_birth <= 2023:
    print("There has been one Democratic Party presidents in office since you were born.")

#Which US President was in office when they were born (1980 onward)
if year_of_birth >= 1980 and year_of_birth <= 1981:
    print("Jimmy Carter was president on your year of birth.")
if year_of_birth >= 1982 and year_of_birth <= 1989:
    print("Ronald Reagan was president on your year of birth.")
if year_of_birth >= 1990 and year_of_birth <= 1993:
    print("George Bush was president on your year of birth.")
if year_of_birth >= 1994 and year_of_birth <= 2001:
    print("Bill Clinton was president on your year of birth.")
if year_of_birth >= 2002 and year_of_birth <= 2009:
    print("George W. Bush was president on your year of birth.")
if year_of_birth >= 2010 and year_of_birth <= 2017:
    print("Barack Obama was president on your year of birth.")
if year_of_birth >= 2018 and year_of_birth <= 2021:
    print("Donald Trump was president on your year of birth.")
if year_of_birth >= 2022 and year_of_birth <= 2023:
    print("Joe Biden was president on your year of birth.")

#Can you think of another approach to #7 and/or #8 that you could have tried? Why is yours better? If you could not get #7/#8 to work, use this question to explain what you were trying to do.
#I'm sure there is many better ones with less rows, but I'm already overwhelmed and cannot figure them out
#I think I could bring a table with the years and presidents and work with that, but don't know how



