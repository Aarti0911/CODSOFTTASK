from tkinter import *
from tkinter import messagebox,simpledialog
from PIL import ImageTk,Image
import random

def ask_username():
    global user_name
    user_name=simpledialog.askstring("Input","Enter your name: ")
    if user_name:
        user_name_label.config(text=user_name)
    else:
        user_name_label.config(text="User")

def restart_game():
    global user_score,comp_score
    user_score = 0
    comp_score = 0
    user_score_label.config(text=user_score)
    comp_score_label.config(text=comp_score)
    win_label.config(text="PLAY!")
    user_choice_label.config(text="Your Choice..")
    comp_choice_label.config(text="Computer's Choice..")
    user_img_label.config(image=user_rock_img)
    comp_img_label.config(image=comp_rock_img)

def restart_clicked(event):
    restart_game()
    messagebox.showwarning("Warning","Game is restarted!")

def declare_winner(user,comp):
    global user_score, comp_score
    if user == comp:
        win_label.config(text="Match Tied!")
    elif user == "rock":
        if comp == "paper":
            comp_score += 1
            comp_score_label.config(text=comp_score)
            win_label.config(text="Computer Won!")
        else:
            user_score +=1
            user_score_label.config(text=user_score)
            win_label.config(text="You Won!")
    elif user == "paper":
        if comp == "rock":
            user_score +=1
            user_score_label.config(text=user_score)
            win_label.config(text="You Won!")
        else:
            comp_score += 1
            comp_score_label.config(text=comp_score)
            win_label.config(text="Computer Won!")
    elif user == "scissor":
        if comp == "paper":
            user_score += 1
            user_score_label.config(text=user_score)
            win_label.config(text="You Won!")
        else:
            comp_score +=1
            comp_score_label.config(text=comp_score)
            win_label.config(text="Computer Won!")
    else:
        pass

def players_turn(user_turn):
    possible_choice =["rock","paper","scissor"]
    comp_turn = random.choice(possible_choice)
    if comp_turn == "rock":
      comp_img_label.config(image=comp_rock_img)
      comp_choice_label.config(text="Computer choose ROCK!")
    elif comp_turn == "paper":
       comp_img_label.config(image=paper_img)
       comp_choice_label.config(text="Computer choose PAPER!")
    else:
       comp_img_label.config(image=comp_scissor_img)
       comp_choice_label.config(text="Computer choose SCISSOR!")
    if user_turn == "rock":
      user_img_label.config(image=user_rock_img)
      user_choice_label.config(text="You choose ROCK!")
    elif user_turn == "paper":
       user_img_label.config(image=paper_img)
       user_choice_label.config(text="You choose PAPER!")
    else:
       user_img_label.config(image=user_scissor_img)
       user_choice_label.config(text="You choose SCISSOR!")
    declare_winner(user_turn,comp_turn)
    check_game_over()

def check_game_over(): #set the number of rounds accordingly
    if user_score == 5:
        messagebox.showinfo("Info","You Won! Game is Restarted")
        restart_game()
    elif comp_score == 5:
        messagebox.showinfo("Info","Computer Won! Game is Restarted")
        restart_game()
    else:
        pass

root = Tk()
root.title("ROCK PAPER SCISSOR")
root.geometry("850x500")
root.resizable(False,False)
root.config(bg="#ffb6c1")

#Load Imgage
user_rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
comp_rock_img = ImageTk.PhotoImage(Image.open("comp_rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
user_scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
comp_scissor_img = ImageTk.PhotoImage(Image.open("comp_scissor.png"))

# User Choice Image
user_img_canvas = Canvas(root,relief=RIDGE,bg = "#ffb6c1",width =300)
user_img_canvas.grid(row=1,column = 0,rowspan=2,padx=10,pady=10)
user_img_label = Label(user_img_canvas,image=user_rock_img,bg = "#ffb6c1",fg="#ffffff")
user_img_label.pack(side=LEFT)

# Computer Choice Image
comp_img_canvas = Canvas(root, relief=RIDGE,bg = "#ffb6c1")
comp_img_canvas.grid(row=1,column = 2,rowspan=2,padx=10,pady=10)
comp_img_label = Label(comp_img_canvas,image=comp_rock_img,bg = "#ffb6c1",fg="#ffffff")
comp_img_label.pack(side=RIGHT)

# Frame for Player Score
score_frame = Frame(root,relief=RIDGE,bg = "#ffb6c1",width =250,height = 20)
score_frame.grid(row=1,column = 1,padx=10,pady=10)

#User Score
user_score = 0
user_score_label = Label(score_frame,text=user_score,font = ("Ariel",50,"bold"),fg="#ffffff",bg ="#ffb6c1")
user_score_label.grid(row=1,column=1,pady=5)

space_label = Label(score_frame,text="\t\t\t\t\t    ",bg="#ffb6c1",fg="#ffffff")
space_label.grid(row=1, column=2)

#Computer Score
comp_score = 0
comp_score_label = Label(score_frame,text=comp_score,font = ("Ariel",50,"bold"),bg ="#ffb6c1",fg="#ffffff")
comp_score_label.grid(row=1,column=3,pady=5)

#winning statement
win_frame = Frame(root,relief=RIDGE,bg = "#ffb6c1")
win_frame.grid(row=2,column = 1,padx=10,pady=10)
win_label = Label(win_frame,text="PLAY!",font = ("Ariel",20,"bold"),fg="#ffffff",bg ="#ffb6c1")
win_label.grid(row=1,column=1,pady=5)

#user choice statement
user_choice_frame = Frame(root,relief=RIDGE,bg="#ffb6c1")
user_choice_frame.grid(row = 3,column=0)
user_choice_label = Label(user_choice_frame,text="Your Choice..",font = ("Ariel",15,"normal"),bg ="#ffb6c1",fg="#ffffff")
user_choice_label.grid(row =1,column=1)

#computer choice statement
comp_choice_frame = Frame(root,relief=RIDGE,bg="#ffb6c1")
comp_choice_frame.grid(row = 3,column=2)
comp_choice_label = Label(comp_choice_frame,text="Computer Choice..",font = ("Ariel",15,"normal"),bg ="#ffb6c1",fg="#ffffff")
comp_choice_label.grid(row =1,column=1)

#buttons
rock_btn = Button(root,text="Rock",width = 15,height=2,font=("Arial",15,"bold"),bg ="#ffffff",fg="black",command=lambda:players_turn("rock"))
rock_btn.grid(row=5,column=0,padx=5,pady=10)

paper_btn = Button(root,text="Paper",width = 15,height=2,font=("Arial",15,"bold"),bg ="#ffffff",fg="black",command=lambda:players_turn("paper"))
paper_btn.grid(row=5,column=1)

scissor_btn = Button(root,text="Scissor",width = 15,height=2,font=("Arial",15,"bold"),bg ="#ffffff",fg="black",command=lambda:players_turn("scissor"))
scissor_btn.grid(row=5,column=2)

#restarts game
restart_btn = Label(root,text="Restart",width = 15,height=2,cursor="hand2",font=("Arial",20,"underline"),bg ="#ffb6c1",fg="#ffffff")
restart_btn.grid(row=6,column=1)
restart_btn.bind("<Button-1>",restart_clicked)

#Username
user_name_frame = Frame(root,relief=RIDGE,bg="#ffb6c1")
user_name_frame.grid(row = 0,column=0,padx=10,pady=10)
user_name_label = Label(user_name_frame,text="",font = ("Ariel",20,"bold"),bg ="#ffb6c1",fg="#ffffff")
user_name_label.grid(row =1,column=1)
ask_username()

# Computer Name
comp_name_frame = Frame(root,relief=RIDGE,bg="#ffb6c1")
comp_name_frame.grid(row = 0,column=2,padx=10,pady=10)
comp_name_label = Label(comp_name_frame,text="Computer",font = ("Ariel",20,"bold"),bg ="#ffb6c1",fg="#ffffff")
comp_name_label.grid(row =1,column=1)

root.mainloop()