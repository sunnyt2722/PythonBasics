numbers  = [4,7,8]
doubledNumbers = [x * 2 for x in numbers] #This will double all the numbers for numbers list and store in doubleNumbers Lists

print(doubledNumbers)

avengers = ["Ironman", "Hulk", "Doctor Strange" , "Thor", "Captain America", "Spiderman", "Antman", "Vision", "Black Widow", "Clint", "Black Panther"]
avengersWithManAtEnd = [avenger for avenger in avengers if avenger.__contains__("man")]

print(avengersWithManAtEnd)
