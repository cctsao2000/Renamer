import os

keyword = input("請輸入原檔名關鍵字：")
old_filenameExtension = input("請輸入原副檔名（例：.pdf,.docx,.jpg...）：")
keywordlist = [keyword,old_filenameExtension]
n = input("請輸入新檔名：")
new_filenameExtension = input("請輸入新副檔名（例：.pdf,.docx,.jpg...）：")
no = 1
count = 0

filelist = sorted(os.listdir())

print("\n預覽(僅顯示三筆)")
for i in filelist: 
    if all(x in i for x in keywordlist): 
        newname = n + "_" + str(no) + new_filenameExtension
        print(i + "-->" + newname)
        count += 1
        no += 1
    if count >= 3:
        break

permission = input("此動作無法撤銷，確定執行請輸入y\n")

warn = None
no = 1
count = 0
if permission == "y":
    for i in filelist: 
        if all(x in i for x in keywordlist): 
            newname = n + "_" + str(no) + new_filenameExtension
            if warn == None:
                if newname in filelist:
                    warn = input("Warn: 偵測到重複檔名，繼續執行可能導致同名檔案遺失，是否繼續執行?(y/n)")
                    if warn == "y":
                        pass
                    else:
                        print("suspended")
                        exit(0)
            os.rename(i,newname)
            count += 1
            no += 1
    if count>0:
        print("done")
    else:
        print("file not found")
else:
    print("canceled")
    exit(0)