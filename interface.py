import tkinter
from tkinter import *
import mysql.connector

root = Tk()
root.title('To-Do-List')
root.geometry('400x650+400+100')
root.resizable(False,False)

task_list = []

def criar_conexao(comando):

    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='atividades_pessoais',
)

    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    
def AddTask():
    task=task_entry.get()
    task_entry.delete(0, END)
    status=status_entry.get()
    status_entry.delete(0, END)
    resultado = f'{task} - {status}'
    if task:
        with open('Crud/tasklist.txt', 'a') as taskfile:
            taskfile.write(f'\n{resultado}')
        task_list.append(resultado)
        caixa_lista.insert(END, resultado)
        criar_conexao(f'''insert into atividade values('{task}', '{status}')''')



def deletetask():
    global task_list
    
    selected_task = caixa_lista.get(ANCHOR)
    
    if selected_task:
        
        task_list.remove(selected_task)
    
        with open('Crud/tasklist.txt', 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + '\n')

        criar_conexao(f'''DELETE FROM atividade WHERE nome_ativ = '{selected_task.split(" - ")[0]}' ''')
        caixa_lista.delete(ANCHOR)


def updatetask():
    selected_task = caixa_lista.get(ANCHOR)
    if selected_task:
        
        new_task = task_entry.get()
        new_status = status_entry.get()

        new_resultado = f'{new_task} - {new_status}'

        
        index = caixa_lista.curselection()[0]
        caixa_lista.delete(index)
        caixa_lista.insert(index, f"{new_resultado}")

        
        criar_conexao(f'''UPDATE atividade SET nome_ativ = '{new_task}', status_ativ = '{new_status}' WHERE nome_ativ = '{selected_task.split(" - ")[0]}';''')

        
        task_list[index] = new_resultado

        
        with open('Crud/tasklist.txt', 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + '\n')



def openTaskfile():

    
    try:
        global task_list
        with open('Crud/tasklist.txt','r') as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                caixa_lista.insert(END, task)
                caixa_lista.insert(END, status)

    except:
        file=open('Crud/interface.py', 'w')
        file.close()

def Procurar_Task():
    
    search_term = search_entry.get()

    
    caixa_lista.delete(0, END)

    
    for task in task_list:
        if search_term.lower() in task.lower():
            caixa_lista.insert(END, task)

    
    result = cursor.fetchall()
    for row in result:
        task = f"{row[0]} - {row[1]}"
        caixa_lista.insert(END, task)


search_entry = Entry(root, width=13, font='arial 20', bd=0)
search_entry.place(x=10, y=230)


search_button = Button(root, text='Buscar', font='arial 15 bold', width=6, bg='#5a95ff', fg='#fff', bd=0, command=Procurar_Task)
search_button.place(x=161, y=230)


image_icon = PhotoImage(file='Crud/task.png')
root.iconphoto(False, image_icon)

top_image = PhotoImage(file='Crud/topbar.png')
Label(root,image=top_image).pack()

dock_image = PhotoImage(file='Crud/dock.png')
Label(root,image=dock_image, bg='#32405b').place(x=30, y=25)

note_image=PhotoImage(file='Crud/task.png')
Label(root,image=note_image, bg='#32405b').place(x=30,y=25)

heading=Label(root,text='Todas as tarefas', font='arial 20 bold', fg='white', bg='#32405b')
heading.place(x=120, y=20)

frame = Frame(root,width=160,height=40,bg='white' )
frame.place(x=30,y=180)
Tarefa = Label(root, text='Tarefa', font='arial 20 bold', fg='Black')
Tarefa.place(x=65, y=130)

frame_2 = Frame(root,width=160, height=40, bg='white')
frame_2.place(x=210,y=180)
Tarefa = Label(root, text='Status', font='arial 20 bold', fg='Black')
Tarefa.place(x=245, y=130)

task=StringVar()
task_entry=Entry(frame, width=18, font='arial 20',bd=0)
task_entry.place(x=10,y=7)

task_entry.focus()

status=StringVar()
status_entry=Entry(frame_2, width=18, font='arial 20',bd=0)
status_entry.place(x=10,y=7)

status_entry.focus()

button=Button(root,text='ADD',font='arial 15 bold', width=6,bg='#5a95ff', fg='#fff', bd=0,command=AddTask)
button.place(x=161,y=90)

update_icone = PhotoImage(file='Crud/update.png')
update_reduz = update_icone.subsample(8)
update_button = Button(root, image=update_reduz, bd=0, command=updatetask)
update_button.pack(anchor='nw')


frame1=Frame(root,bd=3,width=700,height=280,bg='#32405b')
frame1.pack(pady=(160,0))

caixa_lista = Listbox(frame1,font=('arial',12),width=40,height=16,bg='#32405b', fg='white',cursor='hand2', selectbackground='#5a95ff')
caixa_lista.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

caixa_lista.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=caixa_lista.yview)

openTaskfile()

delete_icone=PhotoImage(file='Crud/delete.png')
Button(root,image=delete_icone,bd=0, command=deletetask).pack(padx=13,pady=13)



root.mainloop()