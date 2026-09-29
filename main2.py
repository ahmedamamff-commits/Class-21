#initialize dictionary
test_dict = {"Codingal" : 2, "is" : 2, "best" : 2, "for" : 2, "Coding" : 1}

print("The original, unchanged dictionary : ", str(test_dict))

#initialize value
K = 2

#Using loop
#Selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

#printing result
print("Frequency of the variable 'K' is: " + str(res))
