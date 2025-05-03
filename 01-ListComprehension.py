
'''
Syntax:

newList = [ expression for item in oldList if condition]

-> Suru ma for loop chalcha 
-> Tespachi Condition Check garcha and if True them tyo Item ko value chai "item" ma aaucha and expression ma jancha and That become new Element of newList

'''


#How List Comprehension is Used in Machine Learning

'''
🔶 1. Convert Labels to Binary
You have a list of labels from a binary classification problem:

labels = ["cat", "dog", "dog", "cat", "cat"]

👉 Use list comprehension to convert this into binary format where "cat" = 0 and "dog" = 1.

'''

labels = ["cat", "dog", "dog", "cat", "cat"]

# newList = []

# for item in labels:
#   if item=="cat":
#     newList.append(0)
#   else:
#     newList.append(1)
    
# print(newList)


#Using List Comprehension

# newList = [1 if item =="dog" else 0 for item in labels]
# print(newList)


'''
🔶 2. Text Preprocessing (Lowercase + Remove Stopwords)

sentence = ["This", "is", "a", "great", "Machine", "Learning", "course"]
stopwords = ["is", "a", "this"]
👉 Use list comprehension to:

Convert all words to lowercase
Remove stopwords
'''

# stopwords = ["is", "a", "this"]
# sentence = ["This", "is", "a", "great", "Machine", "Learning", "course"]

# newList = []

# for item in sentence:
#   if item.lower() not in stopwords:
#     newList.append(item.lower())
      
# print(newList)

#Using List Comprehension

stopwords = ["is", "a", "this"]
sentence = ["This", "is", "a", "great", "Machine", "Learning", "course"]

newList = [ item.lower() for item in sentence if item.lower() not in stopwords]
print(newList)


