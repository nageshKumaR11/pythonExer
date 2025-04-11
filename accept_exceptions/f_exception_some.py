
try :
    file = open("somefile.txt")    # change in file name shows error 
except Exception :
    print("File not found.")
else:
    print('File was found.')
    file_content = file.read()
    print(file_content)
    file.close()
finally:
    print("All done.")    


