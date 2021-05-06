programming_dictionary ={ "Bug" :" An error in a program that prevents the program from running as expected",
"Function" : " A piece of code that you can easily call over and over again.",
123 : "Enter the number...",
}
# if a number, not a string, not double quote

#print (programming_dictionary["Key"]);
# print (programming_dictionary["Bug"]);
print (" ");  
print (" ") ;
# print(programming_dictionary[123]);

# Adding new items to dictionary :
programming_dictionary["Loop"] = " The action of doing something over and over again"
#print (f" Added item : {programming_dictionary}")

# Create an empty dictionary :
empty_dictionary ={}

# Wipe an existing dictionary : 
#programming_dictionary ={}    # empty all items inside dictionary :
#print(f"Now +{programming_dictionary}")

#Edit an item in a dictionary :

programming_dictionary["Bug"] = " A changed !!!!"
print(programming_dictionary)

print(" ")  # make space between code block
#Loop through the dictionary :

#for thing in programming_dictionary:
#print(thing)

print("")

# use key in loop to print each name item and its content

for key in programming_dictionary :
 print (key)               # print only the key name of item
#print(programming_dictionary[key])   # print the content for each key 
 # print (" ")
print (programming_dictionary[key])