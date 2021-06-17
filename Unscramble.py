import tkinter
from tkinter import messagebox
import random

def initial(randomQuestion):
    ''' Configures a random scrambled word '''
    label1.configure(text=randomQuestion)

def check():
    ''' Checks if the word that user input is right or not '''
    global questions, num, answers
    userInput = e1.get()
    print(userInput)
    
    if userInput.lower() == answers[num].lower():
        messagebox.showinfo("Success","Your answer is correct")
    else:
        messagebox.showinfo("Error","Incorrect answer")
        e1.delete(0, tkinter.END)

def reset():
    ''' Resets the question '''
    global questions, answers, num
    num = random.randint(0, len(questions)-1)
    label1.configure(text=questions[num])
    e1.delete(0,tkinter.END)

def solve():
    ''' Tells the answer '''
    global answers, num
    messagebox.showinfo("Answer","The answer is : " + answers[num])


answers = ["Spiderman", "Batman", "Ironman", "Flash", "Thor", "Loki", "Superman"]  # Original words
questions = []  # Scrambled words

for i in answers:
    # Shuffling the letters
    words = list(i)
    random.shuffle(words)
    questions.append(words)

num = random.randint(0, len(questions)-1)  # Selecting a random number

# Creating a tkinter window
window = tkinter.Tk()
window.geometry('500x400')
window.configure(background='#03203C')
window.title("Unscramble")

# Adding a label to the window
label1 = tkinter.Label(window, font='times 25', bg='#03203C', fg='#5DA3FA')
label1.pack(pady = 30, ipady = 10, ipadx = 10, padx = 30)
initial(questions[num]) # Passing a random question

# Setting up an answer box to type in our answer
answer = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable = answer)
e1.pack(ipady = 10, ipadx = 10)

# Creating a check button
button1 = tkinter.Button(window, text = 'Check', width = 15, bg = '#6AC47E',command = check)
button1.pack(pady = 20)

# Creating a reset button
button2 = tkinter.Button(window, text = 'Reset', width = 15,bg = '#DE4839', command = reset)
button2.pack(pady = 20)

# Creating a solve button
button3 = tkinter.Button(window, text = 'Solve', width = 15,bg = '#AF9D5A', command = solve)
button3.pack()

# tkinter loop finished
window.mainloop()
