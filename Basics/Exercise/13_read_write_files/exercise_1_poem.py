#This version takes punctuation into consideration resulting in "and" becoming the true answer for the maximum occurences in the file Poem.

from collections import Counter
import string
def words():
    #Opening a file and reading
    with open("poem.txt", 'r') as file:
        text=file.read()


    #Converting everything to lowercase for the true count
    text=text.lower()

    #Removing punctuation so that they don't get processed in the counter
    text=text.translate(str.maketrans('', '',string.punctuation))

    #Post cleaning splitting it to convert the file into list
    words=text.split()

    #Calculating the total number of words using len as the file is list with str
    total_count=len(words)

    #Using Counter to find frequency of all the words
    word_count=Counter(words)

    max_count=max(word_count.values())
    for word, count in word_count.items():
        if count == max_count:
            print(f"The word with max frquency is/are: '{word}' with maxium occurences of: {count}")

    #print("Total word count is: ",total_count)

words()
