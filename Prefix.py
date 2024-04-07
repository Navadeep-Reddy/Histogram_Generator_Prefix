import sys

input_text = sys.argv[1]

try:
    #List to store words
    L = []
    # read words-histogram.txt
    with open("Write_files/words-histogram.txt", 'r') as f:
        while True:
            q = f.readline()
            if not q:
                break  # exit the loop if the end of file is reached
            x = q.split()
            L.append(x)
        


except FileNotFoundError:
    print("File not found")

except IOError:
    print("Error reading the file")

else:
    M = []
    for a in L:
        if a[0].startswith(input_text):
            M.append([a[0], a[2]])

    M = sorted(M, key = lambda x: int(x[1]), reverse = True)
    for i, j in M:
        print(f"{i} : {j}")
