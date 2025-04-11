
try :
    file = open("some_file.txt")    # change in file name shows error 
except Exception as e:
    print(e)
else:
    print('File was found.')
    file_content = file.read()
    print(file_content)
    file.close()
finally:
    print("All done.")    


