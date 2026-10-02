Dictionary = {
    "Codingal" : 3, "is" : 2, "best" : 1, "for coding" : 4, 
}
Frequency = input("Enter a value from the dictionary that you would like to see the frequency of: ")
Frequency2 = Dictionary.get(Frequency)
if Frequency2 in Dictionary.values():
    print(f"The frequency of the character you entered is : {Frequency2}")