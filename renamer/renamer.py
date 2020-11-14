import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.messagebox

window = Tk()
window.title("Renamer alpha 1.0")
window.geometry('535x280')
window.resizable(width=0, height=0)

def selectPath():
    path_ = askdirectory()
    path.set(path_)

def preview():
    no = 1
    count = 0
    row = 6
    keywordlist = [k.get(),ex.get()]
    for i in sorted(os.listdir(path.get())): 
        if all(x in i for x in keywordlist): 
            newname = n.get() + "_" + str(no) + ex.get()
            pr = str(i + "-->" + newname)
            Label(window,text = pr,bg="light grey").grid(row = row, column = 0,sticky= "w",columnspan=3,padx=7)
            count += 1
            no += 1
            row += 1
        if count >= 3:
            break
    Button(window, text = "Rename", command = permission).grid(row = 9, column = 2,sticky= "w")

def permission():
    permit = tkinter.messagebox.askokcancel(title="執行提示", message="此動作無法撤銷，是否確定執行?")
    if permit ==True:
        no = 1
        count = 0
        warned = None
        keywordlist = [k.get(),ex.get()]
        for i in sorted(os.listdir(path.get())): 
            if all(x in i for x in keywordlist): 
                newname = n.get() + "_" + str(no) + ex.get()
                if (newname in os.listdir(path.get())) & (warned == None):
                    warn = tkinter.messagebox.askokcancel(title="執行警告", message="偵測到重複檔名，繼續執行可能導致同名檔案遺失，是否繼續執行?")
                    if warn == True:
                        warned == True
                        pass
                    else:
                        break
                os.chdir(path.get())
                os.rename(i,newname)
                count += 1
                no += 1
        if count>0:
            tkinter.messagebox.showinfo(title="執行提示", message="完成")
        else:
            tkinter.messagebox.showerror(title="執行提示", message="無符合更名條件之檔案")
    else:
        tkinter.messagebox.showinfo(title="執行提示",message="暫停執行")

path = StringVar()
k = StringVar()
ex = StringVar()
n = StringVar()

Label(window,text = "Folder:").grid(row = 0, column = 0,sticky= "w",padx=5)
Entry(window, textvariable = path).grid(row = 0, column = 1,sticky= "w")
Button(window, text = "Browse", command = selectPath).grid(row = 0, column = 2,sticky= "w")

Label(window,text = "請輸入原檔名關鍵字：").grid(row = 1, column = 0,sticky= "w",padx=5)
key = Entry(window,textvariable = k).grid(row = 1, column = 1,sticky= "w")
Label(window,text = "請輸入原副檔名（例：.pdf,.docx,.jpg...）：").grid(row = 2, column = 0,sticky= "w",padx=5)
extension = Entry(window,textvariable = ex).grid(row = 2, column = 1,sticky= "w")
Label(window,text = "請輸入新檔名：").grid(row = 3, column = 0,sticky= "w",padx=5)
name = Entry(window,textvariable = n).grid(row = 3, column = 1,sticky= "w")

Button(window, text = "Preview", command = preview).grid(row = 3, column = 2,sticky= "w")

preview = PanedWindow(window,width=100,height=130,bg="light grey").grid(row = 5, column = 0,columnspan=3,rowspan=4,sticky= "wens",padx=5, pady=5)
previewResult = Label(preview,text = "預覽(顯示上限三筆)：",bg="light grey").grid(row = 5, column = 0,sticky= "w",columnspan=3,padx=7)

window.mainloop()