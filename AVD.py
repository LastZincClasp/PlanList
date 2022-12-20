import tkinter as tk

class R:
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("PLANNING--GARWAY-ING")
        self.root.geometry("320x300")
        self.root.resizable(1, 1)

        self.lb = tk.Listbox(self.root, exportselection=0)
        #self.lb.pack(anchor="nw", side=tk.LEFT)
        self.lb.bind("<<ListboxSelect>>", self.bfollow)
        self.lt = tk.Listbox(self.root, exportselection=0)
        self.lt.bind("<<ListboxSelect>>", self.tfollow)
        #self.lt.pack(anchor="nw", side=tk.RIGHT)
        self.test()

        self.sbY = tk.Scrollbar(self.root, orient=tk.VERTICAL)
        #self.sbY.pack(anchor="ne" ,side=tk.RIGHT, fill=tk.Y)
        #self.sbY.config(command=lambda y, z, x=self, : (x.lb.yview, x.lt.yview))
        self.sbY.config(command=self.yview)
        self.lb.config(yscrollcommand=self.bscry)
        self.lt.config(yscrollcommand=self.tscry)

        self.sbX = tk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        #self.sbX.pack(side=tk.BOTTOM, fill=tk.X)
        self.sbX.config(command=self.xview)
        self.lb.config(xscrollcommand=self.bscrx)
        self.lt.config(xscrollcommand=self.tscrx)

        self.bAdd = tk.Button(self.root, text="Add-Plan", command=self.Add)
        #self.bAdd.pack()

        self.bDel = tk.Button(self.root, text="Fin-Plan", command=self.Del)
        #self.bDel.pack()

        self.lb.place(x=3, y=5)
        self.lt.place(x=151, y=5)
        self.sbY.place(x=300, y=5, height=180)
        self.sbX.place(x=3, y=195, width=300)
        self.bAdd.place(x=55, y=230)
        self.bDel.place(x=205, y=230)

        self.status = 1

    
    def Add(self):
        if self.status == 1:
            self.status = 0
            self.nrot = tk.Toplevel(self.root)
            self.nrot.geometry("250x150")
            #self.nrot.resizable(0, 0)
            self.nrot.title("Add-Plan")
            self.nrot.protocol("WM_DELETE_WINDOW", self.staini)

            self.lname = tk.Label(self.nrot, text="NAME >")
            self.ltime = tk.Label(self.nrot, text="TIMES >")

            self.name = tk.Entry(self.nrot)
            self.time = tk.Entry(self.nrot)

            self.subm = tk.Button(self.nrot, text="Apply",command=self.Apply)

            self.lname.pack(anchor="nw")
            self.name.pack(anchor="ne")
            self.ltime.pack(anchor="sw")
            self.time.pack(anchor="se")
            self.subm.pack()

        else:
            pass
    
    def staini(self):
        self.status = 1
        self.nrot.destroy()

    def Apply(self):
        name = self.name.get()
        time = self.time.get()

        try:
            time = int(time)
        except:
            return None

        if name == "" or time == "" or time <= 0:
            return None

        self.lb.insert(0, name)
        self.lt.insert(0, time)

        self.staini()


    def Del(self):
        if self.status == 1:
            index = self.lb.curselection()
            if index == tuple():
                return None
            index = index[0]

            try:
                index = int(index)
                time = int(self.lt.get(index))
            except ValueError as asdf:
                print(asdf)
                return None
            
            if time - 1 != 0:
                time -= 1
                self.lt.delete(index)
                self.lt.insert(index, time)
            else:
                self.lb.delete(index)
                self.lt.delete(index)
    
    def bfollow(self, *args):
        index = self.lb.curselection()
        if index == tuple():
            return None
        index = int(index[0])
        self.lt.select_clear(0, self.lt.size()-1)
        self.lt.selection_set(index)

    def tfollow(self, *args):
        index = self.lt.curselection()
        if index == tuple():
            return None
        index = int(index[0])
        self.lb.select_clear(0, self.lb.size()-1)
        self.lb.selection_set(index)

    def bscry(self, *args):
        if self.lt.yview() != self.lb.yview():
            self.lt.yview_moveto(args[0])
        self.sbY.set(*args)

    def tscry(self, *args):
        if self.lb.yview() != self.lt.yview():
            self.lb.yview_moveto(args[0])
        self.sbY.set(*args)

    def yview(self, *args):
        self.lt.yview(*args)
        self.lb.yview(*args)

    def bscrx(self, *args):
        if self.lt.xview() != self.lb.xview():
            self.lt.xview_moveto(args[0])
        self.sbX.set(*args)

    def tscrx(self, *args):
        if self.lb.xview() != self.lt.xview():
            self.lb.xview_moveto(args[0])
        self.sbX.set(*args)

    def xview(self, *args):
        self.lt.xview(*args)
        self.lb.xview(*args)


    def loop(self):
        self.root.mainloop()

    def test(self):
        try:
            file = open("./每日任务.txt", encoding="utf-8")
            content = file.read()
            file.close()
            content = content.split("\n")[:-1]
            #print(content)
            for i in range(len(content)):
                #print(content[i])
                content[i] = content[i].split(" ")
                #print(content[i])
                try:
                    content[i][1] = int(content[i][1])
                    if content[i][1] <= 0:
                        break
                except:
                    return None
                self.lb.insert("end", content[i][0])
                self.lt.insert("end", content[i][1])
        except:
            for i in range(1, 101):
                self.lb.insert("end", i + 11451419198101145141919810)
                self.lt.insert("end", i)

if __name__ == "__main__":
    r = R()
    r.loop()