#importing all the modules
import sys
import os
import glob


#Dictionary to store histogram
hist = {}

#Making list for storing all words with duplicates
words = []

#Store the list of text files from a folder
text_files = glob.glob(os.path.join(sys.argv[1], "**/*.txt"), recursive = True)

for input_file in text_files:
    #Opening the text file to count frequencies
    with open(input_file, errors="ignore") as f:
        # Reading lines as elemts of a list
        a = f.readlines()

        # Iterating through each line
        for i in a:

            # Splitting each line into words
            x = i.split()
            
            #Looping through the List of words to remove the  punctuations
            for k in range(0, len(x)):
                if x[k][-1] in ['!', ',', '.', '?']:
                    x[k] = x[k][0: len(x[k]) - 1]

            for word in x:
                #Adding all words to a list
                words.append(word)
                #Adding one if it already exits
                if word in hist.keys():
                    hist[word] += 1
                #Creating new one if it doesn't exit already
                else:
                    hist[word] = 1


#Eliminating duplicates (Do this after getting words from all text files)
unique_words = list(set(words))

#Count the frequency of each unique word in the words list and updating the dictionary
for w in unique_words:
    count = words.count(w)
    hist[w] = count

#Subsection one where you write all the given words into words.txt
with open("Write_files/words.txt", 'w') as f:
    for i in unique_words:
        f.write(i)
        f.write("\n")

#Subsection two where you write the frequency
with open('Write_files/words-histogram.txt', 'w') as f:
    for key, value in hist.items():
        freq = f"{key} : {value}"
        f.write(freq)
        f.write('\n')


