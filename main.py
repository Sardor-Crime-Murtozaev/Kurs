from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk



class SampleAPP(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, TestPage, Page4, Page5, Page6,Page7,Page8):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.backGroundImage=PhotoImage(file=r"1233.png")
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x= -50,y=0)
        self.controller = controller
        self.controller.title("Мой склад")
        self.controller.state("normal")





        headingLabel1 = tk.Label(self, text="Проект СКЛАДА!!!", font=("Times New Roman", 55, "bold"))
        headingLabel1.pack(pady=30)

        my_login2="user1"
        my_login="Admin"
        my_login1="Vip"
        
        login_label = tk.Label(self, text="Введите Логин", font=("Times New Roman", 15, "bold"), bg="#82F0E2")
        login_label.pack(pady=10)

        login_entry = tk.Entry(self, textvariable=my_login, font=("Times New Roman", 15, "bold"))
        login_entry.pack()

        password_label=tk.Label(self,text="Введите Ваш пароль",font = ("Times New Roman", 15, "bold"),bg="#82F0E2")
        password_label.pack()
        

        my_password2="7777"
        my_password1="8888"
        my_password="9999"
        
        password_entry=tk.Entry(self,textvariable=my_password,font = ("Times New Roman", 15, "bold"))
        password_entry.pack()
        def check_password():
            if password_entry.get()== my_password and login_entry.get()==my_login:
            
                controller.show_frame("MenuPage")
            if password_entry.get()== my_password1 and login_entry.get()==my_login1:

                controller.show_frame("TestPage")
            if password_entry.get()==my_password2 and login_entry.get()==my_login2:

                controller.show_frame("Page4")
            else:
                wrong_password_label.config(text="Wrong Password", bg = "#F40909")




        input_button=tk.Button(self,text="Войти",font = ("Times New Roman", 15, "bold"), bg = "#4BF2C6",command=check_password)
        input_button.pack()
        wrong_password_label=tk.Label(self,text="Enter ur Password",font = ("Times New Roman", 15, "bold"),bg="#00891D")
        wrong_password_label.pack()

#Админка
class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.backGroundImage=PhotoImage(file=r"16690.png")
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)
        self.controller = controller
        #headingLabel1 = tk.Label(self, text="АДМИН", font=("Times New Roman", 55, "bold"))
        #headingLabel1.pack(pady=30)
        def page_return():
            controller.show_frame("StartPage")
        return_button = tk.Button(self,text="main menu",font = ("Times New Roman", 15, "bold"), bg = "#00E5BD",command=page_return)
        return_button.place(x=10,y=30)


        def Items():
          controller.show_frame("Page5")
        btn = tk.Button(self, text="Управление Товарами!",font = ("Times New Roman", 15, "bold"),bg="#C2C2C2")
        btn.config(command=Items)
        btn.place(x=55,y=260, width=300,height=50)
        
        def GButton_855_command():
          controller.show_frame("Page6")
        
        GButton_855=tk.Button(self)
        GButton_855["bg"] = "#C2C2C2"
        ft = tkFont.Font(family='Times New Roman',size=15)
        GButton_855["cursor"] = "fleur"
        GButton_855["font"] = ft
        GButton_855["fg"] = "#000000"
        GButton_855["justify"] = "center"
        GButton_855["text"] = "Список заказов"
        GButton_855.place(x=55,y=320,width=300,height=50)
        GButton_855["command"] =GButton_855_command

        def Items1():
          controller.show_frame("Page7")
        btn1 = tk.Button(self, text="Персональные данные!",font = ("Times New Roman", 15, "bold"),bg="#C2C2C2")
        btn1.config(command=Items1)
        btn1.place(x=55,y=380, width=300, height=50)

        def Items2():
          controller.show_frame("Page8")
        btn2 = tk.Button(self, text="Задание",font = ("Times New Roman", 15, "bold"),bg="#C2C2C2")
        btn2.config(command=Items2)
        btn2.place(x=55,y=440, width=300, height=50)

###########################################################


        def Items3():
          controller.show_frame("Page5")
        btn3 = tk.Button(self, text="Управление правами",font = ("Times New Roman", 15, "bold"),bg="#870000")
        btn3.config(command=Items3)
        btn3.place(x=550,y=260, width=300,height=50)

        def Items4():
          controller.show_frame("TestPage")
        btn4 = tk.Button(self, text="Архив заказов",font = ("Times New Roman", 15, "bold"),bg="#B1ECA4")
        btn4.config(command=Items4)
        btn4.place(x=550,y=320, width=300,height=50)

        def Items5():
          controller.show_frame("TestPage")
        btn5 = tk.Button(self, text="Отгрузга",font = ("Times New Roman", 15, "bold"),bg="#B1ECA4")
        btn5.config(command=Items5)
        btn5.place(x=550,y=380, width=300,height=50)

        def Items6():
          controller.show_frame("TestPage")
        btn6 = tk.Button(self, text="Приход новых товаров",font = ("Times New Roman", 15, "bold"),bg="#B1ECA4")
        btn6.config(command=Items6)
        btn6.place(x=550,y=440, width=300,height=50)

    


        


############################################################################

class TestPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.backGroundImage=PhotoImage(file=r"lala.png")
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)
        self.controller = controller
        headingLabel1 = tk.Label(self, text="Зона теста", font=("Times New Roman", 55, "bold"))
        headingLabel1.pack(pady=30)
        
        def page_return():
            controller.show_frame("StartPage")
        return_button = tk.Button(self,text="main menu",font = ("Times New Roman", 15, "bold"),command=page_return)
        return_button.pack(pady=30)

        balance_entry=tk.Entry(self,font = ("Times New Roman", 15, "bold"))
        balance_entry.pack(pady=30)
        def balance_check():
            balance_label = tk.Label(self, text=balance_entry.get(), font=("Times New Roman", 15, "bold"),bg="#ffdfc4")
            balance_label.pack()
        balance_button=tk.Button(self,text="Пишите что хотите",font = ("Times New Roman", 15, "bold"),bg = "#E70000",command=balance_check)
        balance_button.pack(pady=15)

########################################################################

class Page4(tk.Frame):
  def __init__(self,parent,controller):
    tk.Frame.__init__(self,parent)
    self.backGroundImage=PhotoImage(file=r"lala.png")
    self.backGroundImageLabel=Label(self,image=self.backGroundImage)
    self.backGroundImageLabel.place(x=0,y=0)
    
    def page_return():
        controller.show_frame("StartPage")
    return_button = tk.Button(self,text="Главный меню",font = ("Times New Roman", 15, "bold"), bg = "#34CF1C",command=page_return)
    return_button.pack(pady=30)
    
    def Items2():
          controller.show_frame("Page8")
    btn2 = tk.Button(self, text="Задание",font = ("Times New Roman", 15, "bold"),bg="#C2C2C2")
    btn2.config(command=Items2)
    btn2.place(x=55,y=250, width=300, height=50)

    ###############################################################
class Page5(tk.Frame):
    def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       self.backGroundImage=PhotoImage(file=r"199.png")
       self.backGroundImageLabel=Label(self,image=self.backGroundImage)
       self.backGroundImageLabel.place(x=0,y=0)
       def page_return():
          controller.show_frame("MenuPage")
       return_button = tk.Button(self,text="Назад",font = ("Times New Roman", 15, "bold"),command=page_return)
       return_button.pack(pady=250)


       

       def delete():
           selection = languages_listbox.curselection()

           languages_listbox.delete(selection[0])

       def add():
           new_language = language_entry.get()
           languages_listbox.insert(0, new_language)
       language_entry = tk.Entry(self,width=40)
       language_entry.place(x=50,y=150, width=400, height=25)
       add_button = Button(self,text="Добавить", command=add).place(x=50,y=125, width=400, height=25)
       languages_listbox = tk.Listbox(self)
       languages_listbox.place(x=50,y=200, width=400, height=300)
       languages_listbox.insert(END, "Тримол")
       languages_listbox.insert(END, "Фленокс")
       languages_listbox.insert(END, "Фаниган")
       languages_listbox.insert(END, "Боботик")
       languages_listbox.insert(END, "Фленокс")
       languages_listbox.insert(END, "Блокард")

       delete_button = tk.Button(self,text="Удалить", command=delete).place(x=50,y=175, width=400, height=25)

#####################################################################

class Page6(tk.Frame):
    def __init__(self,parent,controller):
      tk.Frame.__init__(self,parent)
      self.backGroundImage=PhotoImage(file=r"tovari1.png")
      self.backGroundImageLabel=Label(self,image=self.backGroundImage)
      self.backGroundImageLabel.place(x=-500,y=0)



      def page_return():
          controller.show_frame("MenuPage")
      return_button = tk.Button(self,text="Назад",font = ("Times New Roman", 15, "bold"),command=page_return)
      return_button.pack(pady=30)
      
      def add_item():
          box.insert(END, entry.get())
          entry.delete(0, END)
 
 
      def del_list():
          select = list(box.curselection())
          select.reverse()
          for i in select:
            box.delete(i)
 
 
      def save_list():
          f = open('spisok.txt', 'w')
          f.writelines("\n".join(box.get(0, END)))
          f.close()
      def load_list():
          f = open("spisok.txt","r")
          for x in f:
            box.insert(END,x)
            print(x)
          f.close()
 

 
      box = Listbox(self,selectmode=EXTENDED)
      box.pack(side=LEFT, fill=Y )
      scroll = Scrollbar(self,command=box.yview)
      scroll.pack(side=LEFT, fill=Y)
      box.config(yscrollcommand=scroll.set)


 
      f = Frame(self)
      
      f.pack(side=LEFT, padx=10)
      entry = Entry(f)
      entry.pack(anchor=N)
      Button(f, text="Добавить", command=add_item)\
    .pack(fill=X)
      Button(f, text="Удалить", command=del_list)\
    .pack(fill=X)
      Button(f, text="Сохранить", command=save_list)\
    .pack(fill=X)
      Button(f, text="Загрузить", command=load_list)\
    .pack(fill=X)    

      box1 = Listbox(self,selectmode=EXTENDED)
      box1.pack(side=RIGHT, fill=Y )
      scroll1 = Scrollbar(self,command=box.yview)
      scroll1.pack(side=RIGHT, fill=Y)
      box1.config(yscrollcommand=scroll.set)
    








#####################################################
class Page7(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.backGroundImage=PhotoImage(file=r"register1.png")
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=-500,y=0)



        def page_return():
          controller.show_frame("MenuPage")
        return_button = tk.Button(self,text="Назад",font = ("Times New Roman", 15, "bold"),command=page_return)
        return_button.pack(pady=30)

        fields = ["Имя", "Фамилия", "Телефон", "Email"]
        labels = [tk.Label(self, text=f) for f in fields]
        entries = [tk.Entry(self) for _ in fields]
        self.widgets = list(zip(labels, entries))
        self.submit = tk.Button(self, text="Сохранить",
                                command=self.print_info)

        for i, (label, entry) in enumerate(self.widgets):
            label.pack()
            entry.pack()
        self.submit.pack()

    def print_info(self):
        for label, entry in self.widgets:
            print("{} = {}".format(label.cget("text"), entry.get()))



#####################################################
class Page8(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.backGroundImage=PhotoImage(file=r"lala.png")
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)
        def page_return():
          controller.show_frame("MenuPage")
        return_button = tk.Button(self,text="Назад",font = ("Times New Roman", 15, "bold"),command=page_return)
        return_button.pack(pady=30)
        

        todos = {
            "Зав.Склад": ["Проверка сотрудников начало работы", "Срочная сборка для особых клиентов"],
            "Оператор": ["в 12:00 Собрание ", "Взять собой отчёты", ""],
            "Доставщик": ["Доставить все заказы во время и качественно"]
        }

        self.notebook = ttk.Notebook(self, width=450, height=330, padding=10)
        for key, value in todos.items():
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=key, underline=0,
                              sticky=tk.NE + tk.SW)
            for text in value:
                ttk.Label(frame, text=text).pack(anchor=tk.W)
        self.label = ttk.Label(self)

        self.notebook.pack()
        self.label.pack(anchor=tk.W)
        self.notebook.enable_traversal()
        self.notebook.bind("<<NotebookTabChanged>>", self.select_tab)

    def select_tab(self, event):
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")
        text = "Ваш текущий выбор: {}".format(tab_name)
        self.label.config(text=text)



  ############################################






    
if __name__ == "__main__":
    app = SampleAPP()
    app.mainloop()

