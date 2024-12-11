import os
print ("This program will help in easy accesing of files")
print ("")
print ("Choose from the options given below:")
print ("1.MS Word")
print ("2.Google Chrome")
print ("3.Study Folder")
x=int(input("Input your choice: "))
while True:
    if x==1:
        os.startfile('C:\Program Files (x86)\Microsoft Office\Office12\WINWORD.EXE')
    if x==3:
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    else:
        print("INVALID")
    
