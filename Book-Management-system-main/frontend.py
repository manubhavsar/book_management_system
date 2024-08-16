from tkinter import *
import backend
import re

def errormessage(error_field):
    '''Error fo'''
    error=Tk()
    error.wm_title("Error")
    error_lable = Label(error,text=f"Invalid {error_field}")
    error_lable.grid(row=1,column=0)
    error.mainloop()



def viewcommand():
    """
    It deletes all the items in the listbox, then inserts the rows returned by the view() function in
    the backend.py file.
    """
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def searchcommand():
    """
    It deletes all the items in the listbox, then inserts the results of the search function into the
    listbox.
    """
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),Price_text.get()):
        list1.insert(END,row)

def add_command():
    """
    It takes the data from the entry boxes and passes it to the backend.insert function
    """
    if Title.get()=="" or Author.get()=="" or Year.get()=="" or Price.get()=="":
        errormessage("(All fields are required)")
    elif len(re.findall("^\d{4}$",year_text.get()))==0:
        errormessage("Year")
    elif len(re.findall("\d+", Price_text.get()))==0:
        errormessage("Price")
    elif len(re.findall("^[a-zA-Z0-9 ]*$", author_text.get()))==0:
        errormessage("Author")
    elif len(re.findall("^[a-zA-Z0-9 ]*$", title_text.get()))==0:
        errormessage("Title")
    
    
    else:
        backend.insert(title_text.get(),author_text.get(),year_text.get(),Price_text.get())
        list1.delete(0,END)
        list1.insert(END,"Press View all to see the new entry")
        viewcommand()

def get_selected_row(event):
    """
    It gets the selected row from the listbox and inserts the values into the entry boxes
    """
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple=list1.get(index)
        
        Title.delete(0,END)
        Title.insert(END,selected_tuple[1])

        Author.delete(0,END)
        Author.insert(END,selected_tuple[2])

        Year.delete(0,END)
        Year.insert(END,selected_tuple[3])

        Price.delete(0,END)
        Price.insert(END,selected_tuple[4])
    except IndexError:
        pass
    

def delete_command():
    """
    It deletes the selected tuple from the database
    """
    try:
        backend.delete(selected_tuple[0])
        Title.delete(0,END)
        Author.delete(0,END)
        Year.delete(0,END)
        Price.delete(0,END)
        viewcommand()
    except NameError:
        errormessage("(No field selected)")

def update_command():
    # Updating the selected tuple in the database and then calling the viewcommand() function to
    # update the listbox.
    try:
        if len(re.findall("^\d{4}$",year_text.get()))==0:
            errormessage("Year")
        elif len(re.findall("\d+", Price_text.get()))==0:
            errormessage("Price")
        elif len(re.findall("^[a-zA-Z0-9 ]+$", author_text.get()))==0:
            errormessage("Author")
        elif len(re.findall("^[a-zA-Z0-9 ]+$", title_text.get()))==0:
            errormessage("Title")
        else:
            backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),Price_text.get())
            viewcommand()
    except NameError:
        errormessage("(No field selected)")
    


window=Tk()


window.wm_title("Bookstore")

Title_Label=Label(window,text="Title")
Title_Label.grid(row=0,column=0)

Author_Label=Label(window,text="Author")
Author_Label.grid(row=0,column=2)

Year_Label=Label(window,text="Year")
Year_Label.grid(row=1,column=0)

Price_Label=Label(window,text="Price")
Price_Label.grid(row=1,column=2)


title_text=StringVar()
Title=Entry(window,textvariable=title_text)
Title.grid(row=0,column=1)


author_text=StringVar()
Author=Entry(window,textvariable=author_text)
Author.grid(row=0,column=3)


year_text=StringVar()
Year=Entry(window,textvariable=year_text)
Year.grid(row=1,column=1)


Price_text=StringVar()
Price=Entry(window,textvariable=Price_text)
Price.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6,)

# Binding the scrollbar to the listbox.
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

view_button=Button(window,text="View all",width=12,command=viewcommand)
view_button.grid(row=2,column=3)


search_button=Button(window,text="Search Entry",width=12,command=searchcommand)
search_button.grid(row=3,column=3)


add_button=Button(window,text="Add Entry",width=12,command=add_command)
add_button.grid(row=4,column=3)


update_button=Button(window,text="Update",width=12,command=update_command)
update_button.grid(row=5,column=3)


delete_button=Button(window,text="Delete",width=12,command=delete_command)
delete_button.grid(row=6,column=3)


exit_button=Button(window,text="Close",width=12,command=window.destroy)
exit_button.grid(row=7,column=3)
window.mainloop()