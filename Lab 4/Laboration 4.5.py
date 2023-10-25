import os

def check_files():

    list = []
    path = input("Enter file directory path: ")
    list = os.listdir(path) 
    list_wrong = []
    text = ""
    sliced_text = ""
    temp = 0

    for i in list:
        if i == "config.xml":
            pass
        else: 
            if len(i) == 28:
                if i[0:13] == "backup-config":
                    text = i
                    sliced_text = text[14:24]
                    sliced_text = sliced_text.replace("-", "") 
                    sliced_text = int(sliced_text)
                    if type(sliced_text) == int:
                        pass
                    else:
                        list_wrong.append(i)
                else:
                    list_wrong.append(i)
            else:
                list_wrong.append(i)
    if len(list_wrong) == 0:
        print("All files follow the format.")
    else: 
        print("These files don't follow the format: ")
        for i in list_wrong:
            print(i)
            
check_files()
