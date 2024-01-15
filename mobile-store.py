from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import webbrowser
from time import strftime




#exit
def on_close():
    exitask = messagebox.askyesno("خروج","آیا میخواهید از برنامه خارج شوید ؟")
    if exitask:
        root.destroy()


app_title = "نرم افزار مدیریت فروشگاه موبایل"

darkmode = False
root = Tk()
root.title(app_title)
root.geometry("1200x800")
root.minsize(1200,800)
root.state("zoomed")
root.config(bg="white")
root.wm_iconbitmap("img/mobile.ico")


#date and time
def datetime():
	string = strftime('%H:%M:%S')
	time_lbl.config(text=string)
	time_lbl.after(1000, datetime)


#buttons color
btn_color = "#1e2c3e"
btn_selected = "#3875de"
btn_clicked_color = "white"
#darkmode color
darkmode_color = "#222233"
default_bg = "white"

web_site = "https://pythonostad.ir/"

name = ["ابوالفضل"]
last_name = ["مزارعی"]
email = ["mail@gmail.com"]
username = ["admin"]
password = ["admin"]

#login frame
login_frame = Frame(root)
login_frame.pack(ipadx=500,ipady=500,fill=BOTH)
login_bg = PhotoImage(file="img/login_bg.png")
login_bg_lbl = Label(login_frame,image=login_bg)
login_bg_lbl.place(y=0,x=0, relwidth=1, relheight=1)

#main buttons frame
main_buttons_frame = Frame(root,bg=btn_color)
main_buttons_frame.pack(side="right",fill=BOTH,ipady=70)
#main window frame
main_window_frame = Frame(root,bg=default_bg)
main_window_frame.pack()


#mobile = 1 , products = 2 , invoice = 3 , settings = 4 , mainpage = 5 , settings = 6
main_buttons = 0



#============================= login and logout =============================#

showpassword = False
show_password_img = PhotoImage(file="img/showpassword.png")
hide_password_img = PhotoImage(file="img/hidepassword.png")
def login_show_password():
    global showpassword
    if showpassword == False:
        show_password_btn.config(image=hide_password_img)
        login_password_ent.config(show="")
        showpassword = True
    else:
        show_password_btn.config(image=show_password_img)
        login_password_ent.config(show="*")
        showpassword = False


def logout():
    
    #login page frame
    login_page_frame = Frame(login_frame,bg=btn_color)
    login_page_frame.pack(expand=True,ipadx=300,ipady=400)

    login_logo_img = PhotoImage(file="img/mobile_main.png")

    #login app logo
    logo = Label(login_page_frame,image=login_logo_img,bg=btn_color)
    logo.place(x=230, y=80)

    #login title label
    login_title_lbl = Label(login_page_frame,text=app_title,fg="white",bg=btn_color,font=("IRANSansDN",18, "bold"))
    login_title_lbl.place(x=120, y=250)


    #username entry
    login_username_ent = ttk.Entry(login_page_frame,width=40,font=("IRANSansDN",11, "bold"))
    login_username_ent.place(x=110, y=350)

    user_name_lbl = Label(login_page_frame,text=":نام کاربری",fg="white",bg=btn_color,font=("IRANSansDN",11, "bold"))
    user_name_lbl.place(x=500 , y=350)

    #password Entry
    login_password_ent = ttk.Entry(login_page_frame,width=40,font=("IRANSansDN",11, "bold"),show="*")
    login_password_ent.place(x=110, y=400)

    password_lbl = Label(login_page_frame,text=":رمزعبور",fg="white",bg=btn_color,font=("IRANSansDN",11, "bold"))
    password_lbl.place(x=500 , y=400)

    #login button
    login_btn = Button(login_page_frame,text="ورود",command=login,width=25,bg="#57a1f8",fg="white",border=0,font=("IRANSansDN",11, "bold"))
    login_btn.place(x=170, y=500)


    #hide and show password
    show_password_btn = Button(login_page_frame,width=15,
                            bg=btn_color,
                            border=0,
                            image=show_password_img,
                            cursor="hand2",
                            command=login_show_password)
    show_password_btn.place(x=70, y=405)
    
        
    
def login():
    #get username and password
    entered_username = login_username_ent.get()
    entered_password = login_password_ent.get()
    #make entrys epmty
    login_username_ent.delete(0, END)
    login_password_ent.delete(0, END)
    
    if entered_username in username and entered_password in password:
        #  for loginform in login_frame.winfo_children():
            login_frame.destroy()
    else:
        messagebox.showerror(title="خطا",message="نام کاربری یا رمزعبور وارد شده اشتباه است")


#login page frame
login_page_frame = Frame(login_frame,bg=btn_color)
login_page_frame.pack(expand=True,ipadx=300,ipady=400)

login_logo_img = PhotoImage(file="img/mobile_main.png")

#login app logo
logo = Label(login_page_frame,image=login_logo_img,bg=btn_color)
logo.place(x=230, y=80)

#login title label
login_title_lbl = Label(login_page_frame,text=app_title,fg="white",bg=btn_color,font=("IRANSansDN",18, "bold"))
login_title_lbl.place(x=120, y=250)


#username entry
login_username_ent = ttk.Entry(login_page_frame,width=40,font=("IRANSansDN",11, "bold"))
login_username_ent.place(x=110, y=350)

user_name_lbl = Label(login_page_frame,text=":نام کاربری",fg="white",bg=btn_color,font=("IRANSansDN",11, "bold"))
user_name_lbl.place(x=500 , y=350)

#password Entry
login_password_ent = ttk.Entry(login_page_frame,width=40,font=("IRANSansDN",11, "bold"),show="*")
login_password_ent.place(x=110, y=400)

password_lbl = Label(login_page_frame,text=":رمزعبور",fg="white",bg=btn_color,font=("IRANSansDN",11, "bold"))
password_lbl.place(x=500 , y=400)

#login button
login_btn = Button(login_page_frame,text="ورود",command=login,width=25,bg="#57a1f8",fg="white",border=0,font=("IRANSansDN",11, "bold"))
login_btn.place(x=170, y=500)


#hide and show password
show_password_btn = Button(login_page_frame,width=15,
                           bg=btn_color,
                           border=0,
                           image=show_password_img,
                           cursor="hand2",
                           command=login_show_password)
show_password_btn.place(x=70, y=405)


#============================= register Page =============================#
def register():
    #get Variables
    reg_name = register_name_ent.get()
    reg_lastname = register_lastname_ent.get()
    reg_username = register_username_ent.get()
    reg_password = register_password_ent.get()
    reg_rt_password = rt_register_password_ent.get()

    #insert data to lists
    if reg_password == reg_rt_password :
        password.append(reg_password)
    elif reg_password != reg_rt_password:
        messagebox.showerror(title="خطا",message="رمزعبور وارد شده با تکرار آن یکسان نیست")

    if not name:
        name.append(reg_name)
    elif reg_name == "":
        messagebox.showerror(title="خطا",message="فیلد نام نمیتواند خالی باشد")
        
    if not last_name:
        last_name.append(reg_lastname)
    elif reg_lastname == "":
        messagebox.showerror(title="خطا",message="فیلد نام خانوادگی نمیتواند خالی باشد")
    
    if not username:
        username.append(reg_username)
    elif reg_password == "":
        messagebox.showerror(title="خطا",message="فیلد رمزعبور نمیتواند خالی باشد")

    
    #epmty Entrys
    register_name_ent.delete(0, END)
    register_lastname_ent.delete(0, END)
    register_username_ent.delete(0, END)
    register_password_ent.delete(0, END)
    rt_register_password_ent.delete(0, END)


    if reg_name !="" and reg_lastname !="" and reg_username !="" and reg_password !="" and reg_rt_password !="" and reg_password == reg_rt_password :
        login_frame.forget()



    #forget login frame
    
reg_pass_show = False
def register_show_password():
    global reg_pass_show
    if reg_pass_show == False:
        show_password_btn.config(image=hide_password_img)
        register_password_ent.config(show="")
        rt_register_password_ent.config(show="")
        reg_pass_show = True
    else:
        show_password_btn.config(image=show_password_img)
        register_password_ent.config(show="*")
        rt_register_password_ent.config(show="*")
        reg_pass_show = False



    
register_logo_img = PhotoImage(file="img/mobile_main.png")

if username == [] and password == []:
    login_page_frame.forget()

    
    #login page frame
    login_page_frame = Frame(login_frame,bg=btn_color)
    login_page_frame.pack(expand=True,ipadx=300,ipady=400)

    #register app logo
    logo = Label(login_page_frame,image=register_logo_img,bg=btn_color)
    logo.place(x=220, y=70)

    #register title label
    register_title_lbl = Label(login_page_frame,text="ثبت نام اولین ورود به نرم افزار",fg="white",bg=btn_color,font=("IRANSansDN",20, "bold"))
    register_title_lbl.place(x=100, y=200)

    #register name 
    register_name_ent = ttk.Entry(login_page_frame,width=40,font=("IRANSansDN",11, "bold"))
    register_name_ent.place(x=100, y=300)

    register_name_lbl = Label(login_page_frame,text=":نام",fg="white",bg=btn_color,font=("IRANSansDN",11, "bold"))
    register_name_lbl.place(x=480 , y=300)

    #register last name 
    register_lastname_ent = ttk.Entry(login_page_frame,width=40,font=("IRANSansDN",11, "bold"))
    register_lastname_ent.place(x=100, y=350)

    register_lastname_lbl = Label(login_page_frame,text=":نام خانوادگی",fg="white",bg=btn_color,font=("IRANSansDN",11, "bold"))
    register_lastname_lbl.place(x=480 , y=350)

    #register username 
    register_username_ent = ttk.Entry(login_page_frame,width=40,font=("IRANSansDN",11, "bold"))
    register_username_ent.place(x=100, y=400)

    user_name_lbl = Label(login_page_frame,text=":نام کاربری",fg="white",bg=btn_color,font=("IRANSansDN",11, "bold"))
    user_name_lbl.place(x=480 , y=400)

    #register password 
    register_password_ent = ttk.Entry(login_page_frame,width=40,font=("IRANSansDN",11, "bold"),show="*")
    register_password_ent.place(x=100, y=450)

    password_lbl = Label(login_page_frame,text=":رمزعبور",fg="white",bg=btn_color,font=("IRANSansDN",11, "bold"))
    password_lbl.place(x=480 , y=450)
    
    #re-type register password 
    rt_register_password_ent = ttk.Entry(login_page_frame,width=40,font=("IRANSansDN",11, "bold"),show="*")
    rt_register_password_ent.place(x=100, y=500)

    rt_password_lbl = Label(login_page_frame,text=":تکرار رمزعبور",fg="white",bg=btn_color,font=("IRANSansDN",11, "bold"))
    rt_password_lbl.place(x=480 , y=500)

    #login button
    register_btn = Button(login_page_frame,text="ثبت نام",command=register,width=39,pady= 7,bg="#57a1f8",fg="white",border=0)
    register_btn.place(x=150, y=600)


    #hide and show password
    show_password_btn = Button(login_page_frame,width=15,
                            bg=btn_color,
                            border=0,
                            image=show_password_img,
                            cursor="hand2",
                            command=register_show_password)
    show_password_btn.place(x=70, y=455)


    

#============================= main Page =============================#
main_page_img = PhotoImage(file="img/main_page.png")
def mainpage():
    global main_buttons,main_page_img
    if main_buttons != 5:
        main_page_btn.config(bg=btn_selected)
        #change main buttons color
        mobile_btn.config(bg=btn_color)
        about_btn.config(bg=btn_color)
        invoice_btn.config(bg=btn_color)
        products_btn.config(bg=btn_color)
        settings_btn.config(bg=btn_color)
        #change main buttons value
        main_buttons = 5

        for item in main_window_frame.winfo_children():
            item.destroy()
        

        #logo
        logo = Label(main_window_frame,image=main_page_img,bg=default_bg)
        logo.pack(pady=20)

        #app name label
        app_name_label = Label(main_window_frame,text=app_title,bg=default_bg,font=("IRANSansDN",16, "bold"))
        app_name_label.pack(pady=20)

        all_products_lbl = Label(main_window_frame,bg=default_bg,text=f"تعداد کل لوازم جانبی : 1 ",font=("IRANSansDN",16, "bold"))
        all_products_lbl.pack(side="right",padx=100,pady=50)

        all_mobile_lbl = Label(main_window_frame,bg=default_bg,text=f"تعداد کل موبایل ها : 1",font=("IRANSansDN",16, "bold"))
        all_mobile_lbl.pack(side="right",padx=100,pady=50)

        all_invoice_lbl = Label(main_window_frame,bg=default_bg,text=f"تعداد کل فاکتورها : 2",font=("IRANSansDN",16, "bold"))
        all_invoice_lbl.pack(side="right",padx=100,pady=50)

#============================= mobile Page =============================#


#mobile page
mobile_id = 1
def mobile():
    global main_buttons,mobile_id,mobile_trv

    if main_buttons != 1:
        #change main buttons color
        mobile_btn.config(bg=btn_selected)
        about_btn.config(bg=btn_color)
        invoice_btn.config(bg=btn_color)
        products_btn.config(bg=btn_color)
        main_page_btn.config(bg=btn_color)
        settings_btn.config(bg=btn_color)
        #change main buttons value
        main_buttons = 1


        for item in main_window_frame.winfo_children():
            item.destroy()
        
        mobile_list_lbl = Label(main_window_frame,text="لیست موبایل",
                               font=("IRANSansDN",30, "bold"),anchor="n",bg="white")
        mobile_list_lbl.grid(row=0,column=3,columnspan=4)

        #tree view
        mobile_trv = ttk.Treeview(main_window_frame,selectmode="browse")
        mobile_trv.grid(row=1,column=3,columnspan=3,padx=20,pady=20)
        mobile_trv["columns"]=("price","imei2","imei1","model","company","id")
        mobile_trv.column("price",width=90,anchor="c")
        mobile_trv.column("imei2",width=90,anchor="c")
        mobile_trv.column("imei1",width=90,anchor="c")
        mobile_trv.column("model",width=90,anchor="c")
        mobile_trv.column("company",width=90,anchor="c")
        mobile_trv.column("id",width=40,anchor="c")
        
        mobile_trv.heading("price",text="قیمت")
        mobile_trv.heading("imei2",text="imei2")
        mobile_trv.heading("imei1",text="imei1")
        mobile_trv.heading("model",text="مدل")
        mobile_trv.heading("company",text="شرکت")
        mobile_trv.heading("id",text="ردیف")

        mobile_trv.insert("","end",iid=mobile_id,
                          values=("8,000,000",2000000000,1000000000,"A32 5G","Samsung",mobile_id))
        
        # mobile company name
        add_mobile_lbl = Label(main_window_frame,text="اضافه کردن موبایل",
                               font=("IRANSansDN",16, "bold"),bg="white")
        add_mobile_lbl.grid(row=2,column=3,columnspan=4)
        mobile_company_lbl = Label(main_window_frame, text=": شرکت موبایل",
                                   font=("IRANSansDN",10),bg="white")
        mobile_company_lbl.grid(row=3,column=6,padx=8,pady=15)

        mobile_company_ent = ttk.Entry(main_window_frame)
        mobile_company_ent.grid(row=3,column=5,padx=8,pady=15)


        # mobile model name
        mobile_model_label = Label(main_window_frame,text=": مدل موبایل",
                                   font=("IRANSansDN",10),bg="white")
        mobile_model_label.grid(row=3,column=4,padx=8,pady=15)

        mobile_model_ent = ttk.Entry(main_window_frame)
        mobile_model_ent.grid(row=3,column=3,padx=8,pady=15)

        # mobile imei 1
        mobile_imei1_lbl = Label(main_window_frame,text=": imei 1",
                                font=("IRANSansDN",10),bg="white")
        mobile_imei1_lbl.grid(row=4,column=6,padx=8,pady=15)

        mobile_imei1_ent = ttk.Entry(main_window_frame)
        mobile_imei1_ent.grid(row=4,column=5,padx=8,pady=15)

        # mobile imei 2
        mobile_imei2_lbl = Label(main_window_frame,text=": imei 2",
                                font=("IRANSansDN",10),bg="white")
        mobile_imei2_lbl.grid(row=4,column=4,padx=8,pady=15)

        mobile_imei2_ent = ttk.Entry(main_window_frame)
        mobile_imei2_ent.grid(row=4,column=3,padx=8,pady=15)

        # mobile price
        mobile_price_lbl = Label(main_window_frame,text=": قیمت فروش",
                                 font=("IRANSansDN",10),bg="white")
        mobile_price_lbl.grid(row=5,column=6,padx=8,pady=15)

        mobile_price_ent = ttk.Entry(main_window_frame)
        mobile_price_ent.grid(row=5,column=5,padx=8,pady=15)
        
        #add button
        mobile_trv_btn = Button(main_window_frame,text="اضافه کردن",
                                font=("IRANSansDN",10),cursor="hand2",height=1,width=15,bg="#57a1f8",fg="white",border=0,command=lambda: mobile_add_data())
        mobile_trv_btn.grid(row=5,column=4,padx=4,pady=15)

        #add button
        mobile_trv_del_btn = Button(main_window_frame,text="حذف",
                                font=("IRANSansDN",10),cursor="hand2",height=1,width=15,bg="#57a1f8",fg="white",border=0,command=lambda: delete_mobile())
        mobile_trv_del_btn.grid(row=5,column=3,padx=4,pady=15)


    #tree view action
    def mobile_add_data():
        global mobile_id
        get_company = mobile_company_ent.get()
        get_model = mobile_model_ent.get()
        get_imei1 = mobile_imei1_ent.get()
        get_imei2 = mobile_imei2_ent.get()
        get_price = mobile_price_ent.get()
        mobile_id += 1

        #insert data
        mobile_trv.insert("","end",
                          values=(get_price,get_imei2,get_imei1,get_model,get_company,mobile_id))
        
        #reset Entrys
        mobile_company_ent.delete(0, END)
        mobile_model_ent.delete(0, END)
        mobile_imei1_ent.delete(0, END)
        mobile_imei2_ent.delete(0, END)
        mobile_price_ent.delete(0, END)
        mobile_company_ent.focus()
        messagebox.showinfo(title="با موفقیت اضافه شد", message="موبایل با موفقیت اضافه شد")

    #delete Mobile
    def delete_mobile():
        del_mobile_ask = messagebox.askyesno(title="حذف اطلاعات",message="از لیست حذف شود ؟")
        if del_mobile_ask:
            selected_mobile = mobile_trv.selection()[0]
            mobile_trv.delete(selected_mobile)
            messagebox.showinfo(title="با موفقیت حذف شد", message="موبایل با موفقیت حذف شد")


#============================= Products Page =============================#
products_id = 1
def products():
    global main_buttons,all_products
    if main_buttons != 2:
        #change main buttons color
        products_btn.config(bg=btn_selected)
        mobile_btn.config(bg=btn_color)
        about_btn.config(bg=btn_color)
        invoice_btn.config(bg=btn_color)
        main_page_btn.config(bg=btn_color)
        settings_btn.config(bg=btn_color)

        #change main buttons value
        main_buttons = 2


        for item in main_window_frame.winfo_children():
            item.destroy()
 
        products_list_lbl = Label(main_window_frame,text="لیست لوازم جانبی",
                               font=("IRANSansDN",30, "bold"),anchor="n",bg="white")
        products_list_lbl.grid(row=0,column=1,columnspan=4)

        #tree view
        products_trv = ttk.Treeview(main_window_frame,selectmode="browse")
        products_trv.grid(row=1,column=1,columnspan=4,padx=20,pady=20)
        products_trv["columns"]=("price","productcode","date","model","company","name","id")
        products_trv.column("price",width=90,anchor="c")
        products_trv.column("productcode",width=90,anchor="c")
        products_trv.column("date",width=90,anchor="c")
        products_trv.column("model",width=90,anchor="c")
        products_trv.column("company",width=90,anchor="c")
        products_trv.column("name",width=120,anchor="c")
        products_trv.column("id",width=40,anchor="c")
        
        products_trv.heading("price",text="قیمت")
        products_trv.heading("productcode",text="کد محصول")
        products_trv.heading("date",text="تاریخ فروش")
        products_trv.heading("model",text="مدل")
        products_trv.heading("company",text="شرکت")
        products_trv.heading("name",text="نام محصول")
        products_trv.heading("id",text="ردیف")

        products_trv.insert("","end",iid=mobile_id,
                          values=("498.000","#456","1402/9/24","EP-TA800","Samsung","شارژر دیواری 25 وات ",mobile_id))
        
        all_products = len(products_trv.get_children())

        add_product_lbl = Label(main_window_frame,text="اضافه کردن لوازم جانبی موبایل",
                               font=("IRANSansDN",16, "bold"),bg="white")
        add_product_lbl.grid(row=2,column=1,columnspan=4)
        
        
        # products name
        product_name_lbl = Label(main_window_frame, text=": نام محصول",
                                   font=("IRANSansDN",10),bg="white")
        product_name_lbl.grid(row=3,column=4,padx=8,pady=15)

        product_name_ent = ttk.Entry(main_window_frame)
        product_name_ent.grid(row=3,column=3,padx=8,pady=15)


        # products company name
        product_company_label = Label(main_window_frame,text=": شرکت",
                                   font=("IRANSansDN",10),bg="white")
        product_company_label.grid(row=4,column=4,padx=8,pady=15)

        product_company_ent = ttk.Entry(main_window_frame)
        product_company_ent.grid(row=4,column=3,padx=8,pady=15)


        # products model name
        product_model_label = Label(main_window_frame,text=": مدل",
                                   font=("IRANSansDN",10),bg="white")
        product_model_label.grid(row=3,column=2,padx=8,pady=15)

        product_model_ent = ttk.Entry(main_window_frame)
        product_model_ent.grid(row=3,column=1,padx=8,pady=15)


        # product code
        product_code_lbl = Label(main_window_frame,text=": کد محصول",
                                font=("IRANSansDN",10),bg="white")
        product_code_lbl.grid(row=4,column=2,padx=8,pady=15)

        product_code_ent = ttk.Entry(main_window_frame)
        product_code_ent.grid(row=4,column=1,padx=8,pady=15)

        # product price
        product_price_lbl = Label(main_window_frame,text=": قیمت فروش",
                                 font=("IRANSansDN",10),bg="white")
        product_price_lbl.grid(row=5,column=4,padx=8,pady=15)

        product_price_ent = ttk.Entry(main_window_frame)
        product_price_ent.grid(row=5,column=3,padx=8,pady=15)

        # products date
        product_date_lbl = Label(main_window_frame,text=": تاریخ",
                                font=("IRANSansDN",10),bg="white")
        product_date_lbl.grid(row=5,column=2,padx=8,pady=15)

        product_date_ent = ttk.Entry(main_window_frame)
        product_date_ent.grid(row=5,column=1,padx=8,pady=15)

        
        #add button
        product_trv_btn = Button(main_window_frame,text="اضافه کردن",
                                font=("IRANSansDN",10),cursor="hand2",height=1,width=15,bg="#57a1f8",fg="white",border=0,command=lambda: product_add_data())
        product_trv_btn.grid(row=7,column=3,padx=8,pady=15)

        #add button
        product_trv_del_btn = Button(main_window_frame,text="حذف",
                                font=("IRANSansDN",10),cursor="hand2",height=1,width=15,bg="#57a1f8",fg="white",border=0,command=lambda: delete_product())
        product_trv_del_btn.grid(row=7,column=2,padx=8,pady=15)


    #tree view action
    def product_add_data():
        global products_id
        get_product_name = product_name_ent.get()
        get_product_company = product_company_ent.get()
        get_product_model = product_model_ent.get()
        get_date = product_date_ent.get()
        get_product_code = product_code_ent.get()
        get_product_price = product_price_ent.get()
        products_id += 1

        #insert data
        products_trv.insert("","end",
                          values=(get_product_price,get_product_code,get_date,get_product_model,get_product_company,get_product_name,products_id))
        
        #reset Entrys
        product_name_ent.delete(0, END)
        product_company_ent.delete(0, END)
        product_model_ent.delete(0, END)
        product_date_ent.delete(0, END)
        product_code_ent.delete(0, END)
        product_price_ent.delete(0, END)
        product_name_ent.focus()
        messagebox.showinfo(title="با موفقیت اضافه شد", message=" با موفقیت اضافه شد")

    #delete product
    def delete_product():
        print(products_trv)
        del_product_ask = messagebox.askyesno(title="حذف اطلاعات",message="از لیست حذف شود ؟")
        if del_product_ask:
            selected_mobile = products_trv.selection()[0]
            products_trv.delete(selected_mobile)
            messagebox.showinfo(title="با موفقیت حذف شد", message=" با موفقیت حذف شد")
            


#============================= Invoice Page =============================#
def invoice():
    global main_buttons,products_trv
    if main_buttons != 3 :
        #change main buttons color
        invoice_btn.config(bg=btn_selected)
        about_btn.config(bg=btn_color)
        mobile_btn.config(bg=btn_color)
        products_btn.config(bg=btn_color)
        main_page_btn.config(bg=btn_color)
        settings_btn.config(bg=btn_color)
        #change main buttons value
        main_buttons = 3

        for item in main_window_frame.winfo_children():
            item.destroy()

        invoice_list_lbl = Label(main_window_frame,text="لیست فاکتورها",
                               font=("IRANSansDN",30, "bold"),anchor="n",bg="white")
        invoice_list_lbl.grid(row=0,column=1,columnspan=4)

        #tree view
        products_trv = ttk.Treeview(main_window_frame,selectmode="browse")
        products_trv.grid(row=1,column=1,columnspan=4,padx=20,pady=20)
        products_trv["columns"]=("price","productcode","date","model","company","name","id")
        products_trv.column("price",width=90,anchor="c")
        products_trv.column("productcode",width=90,anchor="c")
        products_trv.column("date",width=90,anchor="c")
        products_trv.column("model",width=90,anchor="c")
        products_trv.column("company",width=90,anchor="c")
        products_trv.column("name",width=120,anchor="c")
        products_trv.column("id",width=40,anchor="c")
        
        products_trv.heading("price",text="قیمت")
        products_trv.heading("productcode",text="کد محصول")
        products_trv.heading("date",text="تاریخ فروش")
        products_trv.heading("model",text="مدل")
        products_trv.heading("company",text="شرکت")
        products_trv.heading("name",text="نام محصول")
        products_trv.heading("id",text="ردیف")

        products_trv.insert("","end",iid=mobile_id,
                          values=("498.000","#456","1402/9/24","EP-TA800","Samsung","شارژر دیواری 25 وات ",mobile_id))
        

        #add button
        product_trv_btn = Button(main_window_frame,text="پرینت",
                                font=("IRANSansDN",10),width=20,pady= 7,bg="#57a1f8",fg="white",border=0)
        product_trv_btn.grid(row=2,column=1,columnspan=4,pady=10)
 
#============================= about Page =============================#
def openwebsite():
    webbrowser.open_new(web_site)

#about page
def about():
    global main_buttons

    if main_buttons != 4:
        #change main buttons color
        about_btn.config(bg=btn_selected)
        mobile_btn.config(bg=btn_color)
        invoice_btn.config(bg=btn_color)
        products_btn.config(bg=btn_color)
        main_page_btn.config(bg=btn_color)
        settings_btn.config(bg=btn_color)
        #change main buttons value
        main_buttons = 4

        for item in main_window_frame.winfo_children():
            item.destroy()

        #logo
        top_logo = Label(main_window_frame,image=logo_img,bg=default_bg)
        top_logo.pack(pady=20)

        Label(main_window_frame,text=" برنامه مدیریت فروشگاه موبایل ", font=("IRANSansDN", 45),bg=default_bg).pack(pady=20)

        Label(main_window_frame,text="""این برنامه توسط ابوالفضل مزارعی و مهزیار تلیان ساخته شده است \n ایمیل : Abolfazl@gmail.com  \n شماره تماس :  09123456789""",font=("IRANSansDN", 20),bg=default_bg).pack(pady=20)


        site_btn = Button(main_window_frame,text="ورود به وبسایت",
                                font=("IRANSansDN",10),cursor="hand2",width=20,pady= 7,bg="#57a1f8",fg="white",border=0,command=openwebsite)
        site_btn.pack()

#============================= settings page =============================#
set_pass_var = False
def settings():
    global main_buttons
    if main_buttons != 6:
        
        settings_btn.config(bg=btn_selected)
        #change main buttons color
        about_btn.config(bg=btn_color)
        mobile_btn.config(bg=btn_color)
        invoice_btn.config(bg=btn_color)
        products_btn.config(bg=btn_color)
        main_page_btn.config(bg=btn_color)
        #change main buttons value
        main_buttons = 6
        
        for item in main_window_frame.winfo_children():
            item.destroy()
    

              
        #set password check box
        def set_password():
            global set_pass_var
            if set_pass_var == False:
                new_password_entry.config(state="normal")
                retype_new_password_entry.config(state="normal")
                set_pass_var = True
            else:
                new_password_entry.config(state="disabled")
                retype_new_password_entry.config(state="disabled")
                set_pass_var = False

        #set login password

        set_pass_checkbox = Checkbutton(main_window_frame,text="فعال سازی رمز عبور",command=set_password)
        set_pass_checkbox.pack(anchor=NE)


        passText = Label(main_window_frame,text="یک رمز عبور وارد کنید")
        passText.pack(side="right",padx=15)

        new_password_entry = Entry(main_window_frame,show="*",state="disabled")
        new_password_entry.pack(side="right",padx=15)

        rt_passText = Label(main_window_frame,text="رمز عبور را تکرار کنید")
        rt_passText.pack(side="right",padx=15)

        retype_new_password_entry = Entry(main_window_frame,show="*",state="disabled")
        retype_new_password_entry.pack(side="right",padx=15)

        save_pass_btn = Button(main_window_frame,text="ذخیره رمز عبور")
        save_pass_btn.pack(side="right")

        



#============================= Dark Mode =============================#

#drak mode
moon_img = PhotoImage(file="img/moon.png")
sun_img = PhotoImage(file="img/sun.png")


darkmode = False
def dark_mode():
    global darkmode
    if darkmode == False: 

        darkmode_btn.config(image=sun_img) 
        # Changes the window to dark theme 
        root.config(bg=darkmode_color) 
        #frames
        main_window_frame.config(bg=darkmode_color)
        root.config(bg=darkmode_color)
        darkmode = True      
        
    else:
        
        darkmode_btn.config(image=moon_img) 
        # Changes the window to light theme 
        root.config(bg=default_bg) 
        # #frames 
        main_window_frame.config(bg=default_bg)
        root.config(bg=default_bg)
   
        darkmode = False




#============================= Main Page =============================#





#mobile button
main_page_btn = Button(
    main_buttons_frame,
    background=btn_color,
    foreground=btn_clicked_color,
    activebackground=btn_selected,
    activeforeground=btn_clicked_color,
    highlightthickness=2,
    highlightbackground=btn_color,
    width=20,
    height=2,
    border=0,
    cursor="hand2",
    text="صفحه اصلی ",
    font=("IRANSansDN",14, "bold"),
    command=mainpage,
    image=main_page_img,
    compound="right")
main_page_btn.pack(side="top",ipadx=100,ipady=40)

#mobile button
mobile_img = PhotoImage(file="img/mobile.png")
mobile_btn = Button(
    main_buttons_frame,
    background=btn_color,
    foreground=btn_clicked_color,
    activebackground=btn_selected,
    activeforeground=btn_clicked_color,
    highlightthickness=2,
    highlightbackground=btn_color,
    width=20,
    height=2,
    border=0,
    cursor="hand2",
    text="       موبایل ",
    font=("IRANSansDN",14, "bold"),
    command=mobile,
    image=mobile_img,
    compound="right")
mobile_btn.pack(side="top",ipadx=100,ipady=40)

#products button
products_img = PhotoImage(file="img/products.png")
products_btn = Button(
    main_buttons_frame,
    background=btn_color,
    foreground=btn_clicked_color,
    activebackground=btn_selected,
    activeforeground=btn_clicked_color,
    highlightthickness=2,
    highlightbackground=btn_color,
    width=20,
    height=2,
    border=0,
    cursor="hand2",
    text="لوازم جانبی ",
    font=("IRANSansDN",14, "bold"),
    image=products_img,
    command=products,
    compound="right")
products_btn.pack(side="top",ipadx=100,ipady=40)

#invoice button
invoice_img = PhotoImage(file="img/invoice.png")
invoice_btn = Button(
    main_buttons_frame,
    background=btn_color,
    foreground=btn_clicked_color,
    activebackground=btn_selected,
    activeforeground=btn_clicked_color,
    highlightthickness=2,
    highlightbackground=btn_color,
    width=20,
    height=2,
    border=0,
    cursor="hand2",
    text="       فاکتور ",
    font=("IRANSansDN",14, "bold"),
    image=invoice_img,
    command=invoice,
    compound="right")
invoice_btn.pack(side="top",ipadx=100,ipady=40)

#settings button
settings_img = PhotoImage(file="img/settings.png")
settings_btn = Button(
    main_buttons_frame,
    background=btn_color,
    foreground=btn_clicked_color,
    activebackground=btn_selected,
    activeforeground=btn_clicked_color,
    highlightthickness=2,
    highlightbackground=btn_color,
    width=20,
    height=2,
    border=0,
    cursor="hand2",
    text="   تنظیمات ",
    font=("IRANSansDN",14, "bold"),
    image=settings_img,
    compound="right",
    command=settings)
settings_btn.pack(side="top",ipady=40,ipadx=100,fill=BOTH)

#about button
about_img = PhotoImage(file="img/about_us.png")
about_btn = Button(
    main_buttons_frame,
    background=btn_color,
    foreground=btn_clicked_color,
    activebackground=btn_selected,
    activeforeground=btn_clicked_color,
    highlightthickness=2,
    highlightbackground=btn_color,
    width=20,
    height=2,
    border=0,
    cursor="hand2",
    text="       درباره ",
    font=("IRANSansDN",14, "bold"),
    image=about_img,
    compound="right",
    command=about)
about_btn.pack(side="top",ipady=40,ipadx=100,fill=BOTH)

#exit button
exit_img = PhotoImage(file="img/exit.png")
exit_btn = Button(
    main_buttons_frame,
    background=btn_color,
    foreground=btn_clicked_color,
    activebackground=btn_selected,
    activeforeground=btn_clicked_color,
    highlightthickness=2,
    highlightbackground=btn_color,
    width=20,
    height=2,
    border=0,
    cursor="hand2",
    text="خروج ",
    font=("IRANSansDN",14, "bold"),
    image=exit_img,
    compound="right",
    command=on_close)
exit_btn.pack(side="top",ipady=40,ipadx=100,fill=BOTH)


#main page darkmode button
darkmode_btn = Button(
    main_buttons_frame,
    background=btn_color,
    activebackground=btn_color,
    highlightthickness=2,
    highlightbackground=btn_color,
    width=20,
    height=2,
    border=0,
    cursor="hand2",
    image=moon_img,
    command=dark_mode)
darkmode_btn.pack(side="top",ipadx=15,ipady=40,pady=20)



#admin profile img
admin_img = PhotoImage(file="img/profile.png")
admin_profile_img = Label(main_window_frame,bg=default_bg,image=admin_img)
admin_profile_img.pack(anchor="nw",side="left",pady=10,padx=10)

#admin name / lastname/ username profile
admin_profile = Label(main_window_frame,bg=default_bg,text=(name,last_name,"\n",username),justify="left",font=("IRANSansDN",12, "bold"))
admin_profile.pack(anchor="nw",side="left",pady=10)


#date and time 
time_lbl = Label(main_window_frame, font=("IRANSansDN",16, "bold"))
time_lbl.pack(padx=50)

#logo
logo_img = PhotoImage(file="img/mobile_main.png")
logo = Label(main_window_frame,image=logo_img,bg=default_bg)
logo.pack(pady=100)

#app name label
app_name_label = Label(main_window_frame,text=app_title,bg=default_bg,font=("IRANSansDN",16, "bold"))
app_name_label.pack(pady=40)

all_products_lbl = Label(main_window_frame,bg=default_bg,text=f"تعداد کل لوازم جانبی : 1 ",font=("IRANSansDN",16, "bold"))
all_products_lbl.pack(padx=100,pady=50)

all_mobile_lbl = Label(main_window_frame,bg=default_bg,text=f"تعداد کل موبایل ها : 1",font=("IRANSansDN",16, "bold"))
all_mobile_lbl.pack(padx=100,pady=50)

all_invoice_lbl = Label(main_window_frame,bg=default_bg,text=f"تعداد کل فاکتورها : 2",font=("IRANSansDN",16, "bold"))
all_invoice_lbl.pack(padx=100,pady=50)


root.protocol('WM_DELETE_WINDOW',on_close)
datetime()
root.mainloop()