import os

os.system("C:\\Users\\linew\\anaconda3\\python.exe C:\\Users\\linew\\anaconda3\\Scripts\\pyuic5-script.py -x main.ui -o temp.py")
f = open("temp.py", encoding='cp1251')
print(f.read())
f.close()
