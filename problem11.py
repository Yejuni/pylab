

a = ["1: Opens a file for reading only in binary.","2: The file pointer is placed.","3: This is the default mode."]
f = open("C:/Users/주늬요/OneDrive/문서/file.txt", 'w')
try:

    for i in range(0, 3):
        data = a[i]
        f.write(data)
        f.write("\n")
except FileNotFoundError:

    f.close()