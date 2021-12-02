#Pickle Example

import pickle

value = pickle.HIGHEST_PROTOCOL

class Input: pass

x = input()



filehandler = open('data.txt','wb')
pickle.dump(x, filehandler)
filehandler.close()

file = open('data.txt', 'rb')
content = pickle.load(file)
file.close()

print(content)