from tkinter import *
from tkinter.ttk import Notebook
from tkinter.messagebox import askyesno
import time
import random

def frame_des():
    global frame,frame_list
    for i in frame_list:
        i.destroy()
    frame_list=[]
def frame_5_():
    root.destroy()
def frame_4_():
    global frame_list
    frame_des()
    frame_4_1=Notebook(frame,width=261,height=240)
    frame_4_1.place(x=10,y=63)
    frame_4_2=Frame(frame_4_1)
    frame_4_3=Frame(frame_4_1)
    frame_4_1.add(frame_4_2,text="One player",padding=2)
    frame_4_1.add(frame_4_3,text="Two player",padding=2)

    frame_4_8=Scrollbar(frame_4_2)
    frame_4_8.pack(fill="y",side=RIGHT)
    frame_4_9=Scrollbar(frame_4_3)
    frame_4_9.pack(fill="y",side=RIGHT)
    frame_4_6=Text(frame_4_2,font='arial 14',width=24,height=11)
    frame_4_6.pack()
    frame_4_7=Text(frame_4_3,font='arial 14',width=24,height=11)
    frame_4_7.pack()
    frame_4_8.config(command=frame_4_6.yview)
    frame_4_6.config(yscrollcommand=frame_4_8.set)
    frame_4_9.config(command=frame_4_7.yview)
    frame_4_7.config(yscrollcommand=frame_4_9.set)

    with open('data\\one player.txt',mode='r') as f:
        obj=f.read()
        frame_4_6.insert('end',obj)
    with open('data\\two player.txt',mode='r') as f:
        obj=f.read()
        frame_4_7.insert('end',obj)
    frame_4_6.config(state='disable')
    frame_4_7.config(state='disable')

    frame_4_10=Label(frame,text='Score Board',bg='#01CBC6',fg='#000000',font='arial 22 bold underline')
    frame_4_10.place(x=20,y=335)
    frame_4_5=Button(frame,image=image,relief='flat',bg='#01CBC6',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=frame_1_)
    frame_4_5.place(x=220,y=335)
    
    frame_list=[frame_4_6,frame_4_7,frame_4_2,frame_4_3,frame_4_1,frame_4_5,frame_4_10]
def re_play():
    global player_chance,frame_play_3,active_c
    player_chance=1
    pb1_.set(1)
    pb2_.set(2)
    pb3_.set(3)
    pb4_.set(4)
    pb5_.set(5)
    pb6_.set(6)
    pb7_.set(7)
    pb8_.set(8)
    pb9_.set(9)
    frame_play_3.config(text=f'{name1} chance')
def check_condition():
    global name1,name2,player_chance,active_c,score1,score2
    if pb1_.get()==pb2_.get() and pb1_.get()==pb3_.get():
        if player_chance%2==0:
            c=askyesno('win',f'{name1} winner!\nPress yes to restart...') 
            score1.set(score1.get()+1)
        else:
            c=askyesno('win',f'{name2} winner!\nPress yes to restart...') 
            score2.set(score2.get()+1)
    if pb4_.get()==pb5_.get() and pb4_.get()==pb6_.get():
        if player_chance%2==0:
            c=askyesno('win',f'{name1} winner!\nPress yes to restart...') 
            score1.set(score1.get()+1)
        else:
            c=askyesno('win',f'{name2} winner!\nPress yes to restart...') 
            score2.set(score2.get()+1)
    if pb7_.get()==pb8_.get() and pb7_.get()==pb9_.get():
        if player_chance%2==0:
            c=askyesno('win',f'{name1} winner!\nPress yes to restart...') 
            score1.set(score1.get()+1)
        else:
            c=askyesno('win',f'{name2} winner!\nPress yes to restart...') 
            score2.set(score2.get()+1)
    if pb1_.get()==pb4_.get() and pb1_.get()==pb7_.get():
        if player_chance%2==0:
            c=askyesno('win',f'{name1} winner!\nPress yes to restart...') 
            score1.set(score1.get()+1)
        else:
            c=askyesno('win',f'{name2} winner!\nPress yes to restart...') 
            score2.set(score2.get()+1)
    if pb2_.get()==pb5_.get() and pb2_.get()==pb8_.get():
        if player_chance%2==0:
            c=askyesno('win',f'{name1} winner!\nPress yes to restart...') 
            score1.set(score1.get()+1)
        else:
            c=askyesno('win',f'{name2} winner!\nPress yes to restart...') 
            score2.set(score2.get()+1)
    if pb3_.get()==pb6_.get() and pb3_.get()==pb9_.get():
        if player_chance%2==0:
            c=askyesno('win',f'{name1} winner!\nPress yes to restart...') 
            score1.set(score1.get()+1)
        else:
            c=askyesno('win',f'{name2} winner!\nPress yes to restart...') 
            score2.set(score2.get()+1)
    if pb1_.get()==pb5_.get() and pb1_.get()==pb9_.get():
        if player_chance%2==0:
            c=askyesno('win',f'{name1} winner!\nPress yes to restart...') 
            score1.set(score1.get()+1)
        else:
            c=askyesno('win',f'{name2} winner!\nPress yes to restart...') 
            score2.set(score2.get()+1)
    if pb3_.get()==pb5_.get() and pb3_.get()==pb7_.get():
        if player_chance%2==0:
            c=askyesno('win',f'{name1} winner!\nPress yes to restart...') 
            score1.set(score1.get()+1)
        else:
            c=askyesno('win',f'{name2} winner!\nPress yes to restart...') 
            score2.set(score2.get()+1)
    try:
        if c==True:
            if len_name==0:
                with open('data\\one player.txt',mode='r') as f:
                    obj=f.readlines()
                    obj[-2]=f' {score1.get()}            {score2.get()}\n'
                    with open('data\\one player.txt',mode='w') as f1:
                        for i in obj:
                            f1.write(i)
            elif len_name==1:
                with open('data\\two player.txt',mode='r') as f:
                    obj=f.readlines()
                    obj[-2]=f' {score1.get()}            {score2.get()}\n'
                    with open('data\\two player.txt',mode='w') as f1:
                        for i in obj:
                            f1.write(i)
            re_play()
            active_c=c
        else:
            frame_1_()
    except:pass
def computer_chance():
    global player_chance,frame_play_3
    while 1:
        cs=random.randint(1,9)
        print(cs)
        if cs==1 and pb1_.get()=='1':
            pb1_.set('X')
            break
        elif cs==2 and pb2_.get()=='2':
            pb2_.set('X')
            break
        elif cs==3 and pb3_.get()=='3':
            pb3_.set('X')
            break
        elif cs==4 and pb4_.get()=='4':
            pb4_.set('X')
            break
        elif cs==5 and pb5_.get()=='5':
            pb5_.set('X')
            break
        elif cs==6 and pb6_.get()=='6':
            pb6_.set('X')
            break
        elif cs==7 and pb7_.get()=='7':
            pb7_.set('X')
            break
        elif cs==8 and pb8_.get()=='8':
            pb8_.set('X')
            break
        elif cs==9 and pb9_.get()=='9':
            pb9_.set('X')
            break
    player_chance=player_chance+1
    check_condition()
    print('computer chance complete')
    frame_play_3.config(text=f'{name1} chance')
    print(cs,' fghj')
def btn_press(event=0):
    global player_chance,frame_play_3,name1,name2,len_name,active_c,frame_list
    active_c=False
    c=event.widget.cget("text")
    print('enter button press')
    print(c)
    if c=='X' or c=='O':
        frame_list[1].config(text='Already exist position!')
    else:
        frame_list[1].config(text='')
        if player_chance%2==0:
            if c==1:    pb1_.set('X')
            if c==2:    pb2_.set('X')
            if c==3:    pb3_.set('X')
            if c==4:    pb4_.set('X')
            if c==5:    pb5_.set('X')
            if c==6:    pb6_.set('X')
            if c==7:    pb7_.set('X')
            if c==8:    pb8_.set('X')
            if c==9:    pb9_.set('X')
            frame_play_3.config(text=f'{name1} chance')
            player_chance=player_chance+1
            check_condition()
        else:
            if c==1:    pb1_.set('O')
            if c==2:    pb2_.set('O')
            if c==3:    pb3_.set('O')
            if c==4:    pb4_.set('O')
            if c==5:    pb5_.set('O')
            if c==6:    pb6_.set('O')
            if c==7:    pb7_.set('O')
            if c==8:    pb8_.set('O')
            if c==9:    pb9_.set('O')
            frame_play_3.config(text=f'{name2} chance')
            player_chance=player_chance+1
            check_condition()
            if len_name==0 and active_c==False:
                print("computer_chance")
                computer_chance()
def frame_play():
    global frame,frame_list,len_name,player_chance,name1,name2,frame_play_3,score1,score2
    if len(frame_list)==7:
        if len(frame_list[1].get())<=8:
            name1=frame_list[1].get()
        else:
            name1=frame_list[1].get()[0:8]
        if len(frame_list[1].get())<=8:
            name2=frame_list[3].get()
        else:
            name2=frame_list[3].get()[0:8]
        len_name=1
    elif len(frame_list)==5:
        if len(frame_list[1].get())<=8:
            name1=frame_list[1].get()
        else:
            name1=frame_list[1].get()[0:8]
        name2='Computer'
        len_name=0
    #--------------------------------------------
    score1=IntVar()
    score2=IntVar()
    score1.set(0)
    score2.set(0)
    player_chance=1
    pb1_.set(1)
    pb2_.set(2)
    pb3_.set(3)
    pb4_.set(4)
    pb5_.set(5)
    pb6_.set(6)
    pb7_.set(7)
    pb8_.set(8)
    pb9_.set(9)
    if len_name==0:
        with open('data\\one player.txt',mode='a') as f:
            f.write(f'\n {name1}   {name2}')
            f.write(f'\n {score1.get()}            {score2.get()}')
            f.write("\n =====================")
    if len_name==1:
        with open('data\\two player.txt',mode='a') as f:
            f.write(f'\n {name1}   {name2}')
            f.write(f'\n {score1.get()}            {score2.get()}')
            f.write("\n =====================")
    frame_des()
    #--------------------------------------------------------------------
    game_canvas=Canvas(frame,width=200,height=200,bg='#01CBC6',)
    game_canvas.place(x=42,y=80)
    #-------------------------------------------------------------------------------
    Label(game_canvas,image=image2).place(x=0,y=0)
    pb1=Button(game_canvas,textvariable=pb1_,font='arial 18',width=2,padx=13,pady=9,relief='raised',bg='#01CBC6',fg='#000000',activebackground='#1287A5',cursor='hand2')
    pb1.bind('<Button-1>',btn_press)
    pb1.place(x=3,y=3)
    pb2=Button(game_canvas,textvariable=pb2_,font='arial 18',width=2,padx=11,pady=9,relief='raised',bg='#01CBC6',fg='#000000',activebackground='#1287A5',cursor='hand2')
    pb2.bind('<Button-1>',btn_press)
    pb2.place(x=74,y=3)
    pb3=Button(game_canvas,textvariable=pb3_,font='arial 18',width=2,padx=12,pady=9,relief='raised',bg='#01CBC6',fg='#000000',activebackground='#1287A5',cursor='hand2')
    pb3.bind('<Button-1>',btn_press)
    pb3.place(x=140,y=3)
    pb4=Button(game_canvas,textvariable=pb4_,font='arial 18',width=2,padx=13,pady=6,relief='raised',bg='#01CBC6',fg='#000000',activebackground='#1287A5',cursor='hand2')
    pb4.bind('<Button-1>',btn_press)
    pb4.place(x=3,y=74)
    pb5=Button(game_canvas,textvariable=pb5_,font='arial 18',width=2,padx=11,pady=6,relief='raised',bg='#01CBC6',fg='#000000',activebackground='#1287A5',cursor='hand2')
    pb5.bind('<Button-1>',btn_press)
    pb5.place(x=74,y=74)
    pb6=Button(game_canvas,textvariable=pb6_,font='arial 18',width=2,padx=12,pady=6,relief='raised',bg='#01CBC6',fg='#000000',activebackground='#1287A5',cursor='hand2')
    pb6.bind('<Button-1>',btn_press)
    pb6.place(x=140,y=74)
    pb7=Button(game_canvas,textvariable=pb7_,font='arial 18',width=2,padx=13,pady=8,relief='raised',bg='#01CBC6',fg='#000000',activebackground='#1287A5',cursor='hand2')
    pb7.bind('<Button-1>',btn_press)
    pb7.place(x=3,y=140)
    pb8=Button(game_canvas,textvariable=pb8_,font='arial 18',width=2,padx=11,pady=8,relief='raised',bg='#01CBC6',fg='#000000',activebackground='#1287A5',cursor='hand2')
    pb8.bind('<Button-1>',btn_press)
    pb8.place(x=74,y=140)
    pb9=Button(game_canvas,textvariable=pb9_,font='arial 18',width=2,padx=12,pady=8,relief='raised',bg='#01CBC6',fg='#000000',activebackground='#1287A5',cursor='hand2')
    pb9.bind('<Button-1>',btn_press)
    pb9.place(x=140,y=140)
    #-------------------------------------------------------------------------------
    frame_play_0=Label(frame,text='',font='arial 9 bold',fg='#E8290B',bg='#01CBC6')
    frame_play_0.place(x=70,y=284)
    frame_play_1=Button(frame,image=image,relief='flat',bg='#01CBC6',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=frame_1_)
    frame_play_1.place(x=220,y=300)
    frame_play_2=Button(frame,image=image3,relief='flat',bg='#01CBC6',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=re_play)
    frame_play_2.place(x=10,y=300)
    frame_play_3=Label(frame,text=f'{name1} chance',font='arial 12 bold',bg='#01CBC6',fg='#000000')
    frame_play_3.place(x=70,y=300)
    frame_play_4=Label(frame,text=f'{name1}  |  {name2}',font='arial 10 bold',bg='#01CBC6',fg='#000000')
    frame_play_4.place(x=70,y=330)
    frame_play_5=Label(frame,textvariable=score1,font='arial 10 bold',bg='#01CBC6',fg='#000000')
    frame_play_5.place(x=70,y=350)    
    frame_play_6=Label(frame,textvariable=score2,font='arial 10 bold',bg='#01CBC6',fg='#000000')
    frame_play_6.place(x=140,y=350)
    
    frame_list=[game_canvas,frame_play_0,frame_play_1,frame_play_2,frame_play_3,frame_play_4,frame_play_5,frame_play_6]
def frame_3_():
    global frame,frame_list
    frame_des()
    #-------------------------------------------------------------------------------------------------
    frame_3_1=Label(frame,text='Enter 1st player name',font='arial 16 bold',bg='#01CBC6',fg='#000000',width=21)
    frame_3_1.place(x=10,y=100)
    frame_3_2=Entry(frame,font='arial 16',width=15,justify='center',cursor='ibeam',selectbackground='#0A79DF')
    frame_3_2.insert(0,'Player 1')
    frame_3_2.place(x=50,y=135)
    frame_3_3=Label(frame,text='Enter 2nd player name',font='arial 16 bold',bg='#01CBC6',fg='#000000',width=21)
    frame_3_3.place(x=10,y=180)
    frame_3_4=Entry(frame,font='arial 16',width=15,justify='center',cursor='ibeam',selectbackground='#0A79DF')
    frame_3_4.insert(0,'Player 2')
    frame_3_4.place(x=50,y=215)
    frame_3_5=Button(frame,text='Play',font='arial 18',width=10,relief='raised',bg='#E8290B',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=frame_play)
    frame_3_5.place(x=45,y=260)
    frame_3_6=Button(frame,image=image,relief='flat',bg='#01CBC6',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=frame_1_)
    frame_3_6.place(x=200,y=256)
    frame_3_7=Label(frame,text="Enjoy the game\n© 2020 Chetanguptamrt",font='lucida 13',bg='#000000',fg='#FFF222',height=3,width=31)
    frame_3_7.place(x=2,y=327)
    #---------------------------------------------------------------------------------------------------

    frame_list=[frame_3_1,frame_3_2,frame_3_3,frame_3_4,frame_3_5,frame_3_6,frame_3_7]
def frame_2_():
    global frame,frame_list
    frame_des()
    #-------------------------------------------------------------------------------------------------
    frame_2_1=Label(frame,text='Enter player name',font='arial 16 bold',bg='#01CBC6',fg='#000000')
    frame_2_1.place(x=50,y=120)
    frame_2_2=Entry(frame,font='arial 16',width=15,justify='center',cursor='ibeam',selectbackground='#0A79DF')
    frame_2_2.insert(0,'Player 1')
    frame_2_2.place(x=50,y=160)
    frame_2_3=Button(frame,text='Play',font='arial 18',width=10,relief='raised',bg='#E8290B',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=frame_play)
    frame_2_3.place(x=45,y=220)
    frame_2_6=Button(frame,image=image,relief='flat',bg='#01CBC6',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=frame_1_)
    frame_2_6.place(x=200,y=216)
    frame_2_7=Label(frame,text="Enjoy the game\n© 2020 Chetanguptamrt",font='lucida 13',bg='#000000',fg='#FFF222',height=3,width=31)
    frame_2_7.place(x=2,y=327)
    #---------------------------------------------------------------------------------------------------
    frame_list=[frame_2_1,frame_2_2,frame_2_3,frame_2_6,frame_2_7]
def frame_1_():
    global frame,frame_list
    frame_des()
    #----------------------------------------------------------------------------------------------
    frame_1_1=Label(frame,text='Tic Tac Toe',font='algerianregular 28 bold underline',bg='#01CBC6',fg='#000000')
    frame_1_1.place(x=40,y=10)
    frame_1_2=Button(frame,text='One player',font='arial 18',width=13,relief='raised',bg='#1287A5',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=frame_2_)
    frame_1_2.place(x=50,y=100)
    frame_1_3=Button(frame,text='Two player',font='arial 18',width=13,relief='raised',bg='#1287A5',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=frame_3_)
    frame_1_3.place(x=50,y=150)
    frame_1_4=Button(frame,text='Score',font='arial 18',width=13,relief='raised',bg='#1287A5',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=frame_4_)
    frame_1_4.place(x=50,y=200)
    frame_1_5=Button(frame,text='Exit',font='arial 18',width=13,relief='raised',bg='#1287A5',fg='#000000',activebackground='#01CBC6',cursor='hand2',command=frame_5_)
    frame_1_5.place(x=50,y=250)
    frame_1_6=Label(frame,text="Enjoy the game\n© 2020 Chetanguptamrt",font='lucida 13',bg='#000000',fg='#FFF222',height=3,width=31)
    frame_1_6.place(x=2,y=327)
    #---------------------------------------------------------------------------------------------
    frame_list=[frame_1_2,frame_1_3,frame_1_4,frame_1_5,frame_1_6]
if __name__ == "__main__":
    root=Tk()
    root.geometry('300x400+200+100')
    root.resizable(False,False)
    #-----------------------------------menu--------------------
    mainmenu=Menu(root)
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label='One player',command=frame_2_)
    m1.add_command(label='Two player',command=frame_3_)
    m1.add_separator()
    m1.add_command(label='Home',command=frame_1_)
    m1.add_command(label='Score')
    m1.add_separator()
    m1.add_command(label='Exit')
    mainmenu.add_cascade(label='New',menu=m1)
    m2=Menu(mainmenu,tearoff=0)
    m2.add_command(label='About it')
    m2.add_command(label='Contact us')
    m2.add_separator()
    m2.add_command(label='Game Rule')
    mainmenu.add_cascade(label='Help',menu=m2)
    root.config(menu=mainmenu)
    #-----------------------------------frame------------------------------
    frame=Frame(root,width=300,height=400,bd=4,relief='raised',bg='#01CBC6')
    frame.pack()
    image=PhotoImage(file='photos\\back.png')
    image2=PhotoImage(file='photos\\chart.png')
    image3=PhotoImage(file='photos\\play.png')
    pb1_=StringVar()
    pb2_=StringVar()
    pb3_=StringVar()
    pb4_=StringVar()
    pb5_=StringVar()
    pb6_=StringVar()
    pb7_=StringVar()
    pb8_=StringVar()
    pb9_=StringVar()
    frame_list=[]
    frame_1_()
    root.mainloop()