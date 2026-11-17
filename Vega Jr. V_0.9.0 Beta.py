import random
import tkinter as tk

waiting_for_mood = False
waiting_for_favorite_game = False
waiting_for_homework_subject = False
waiting_for_homework_topic = False
grade_step = 0
math_grade = 0
science_grade = 0
history_grade = 0
english_grade = 0

# 0 = not using calculator
# 1 = waiting for math grade
# 2 = waiting for science grade
# 3 = waiting for history grade
# 4 = waiting for english grade


favorite_game = ""
homework_subject = ""


def add_message(message):
    chat.config(state="normal")
    chat.insert(tk.END, message)
    chat.see(tk.END)
    chat.config(state="disabled")
def vega_response(text):
    global waiting_for_mood
    global waiting_for_favorite_game
    global favorite_game
    global waiting_for_homework_subject
    global waiting_for_homework_topic
    global homework_subject
    global grade_step
    global math_grade
    global science_grade
    global history_grade
    global english_grade
    text = text.lower()
    if "hello" in text or \
        "hi" in text or \
        "hey" in text or \
        "greetings" in text or \
        "sup" in text:
        return "HI :D"
    elif waiting_for_favorite_game:
        favorite_game = text
        waiting_for_favorite_game = False
        return "I'll remember that"
    elif "remember my favorite game" in text:
        waiting_for_favorite_game = True
        return "What's your favorite game"
    elif text == "help":
        return "help - shows this message," \
        " hello - greets you," \
        " homework - helps you with your homework," \
        "do it - I can help you with your homework, but not do it for you," \
        " your name - tells you my name," \
        " joke - tells you a joke," \
        " who made you - tells you who made me," \
        " how are you - asks about my mood," \
        " remember my favorite game - remembers your favorite game," \
        " what's my favorite game - tells you your favorite game," \
        " grade calculator - calculates your grade," \
        " coin flip - flips a coin"
    elif "your name" in text \
        or "what's your name" in text \
        or "whats your name" in text:
        return "My name is Little Vega, or Vega Jr."
    elif "who made you" in text \
        or "who created you" in text \
        or "who is your creator" in text:
        return "KNG AKA Kenneth is my creator, with the help of Copilot and some other AI tools"
    elif "joke" in text \
        or "tell me a joke" in text \
        or "make me laugh" in text \
        or "say something funny" in text:
        return random.choice(["A Buddhist monk approaches a hotdog stand and says,"
    " “make me one with everything” XD",
      "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the chicken cross the road? To get to the other side!",
          "What do you call a fake noodle? An Impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
              "Did you hear about the claustrophobic astronaut?• He just needed a little space.",
                "Why did the tomato turn red? Because it saw the salad dressing!",
                  "Why did the coffee file a police report? It got mugged!",
                    "Why did the bicycle fall over? Because it was two-tired!",
                      "Why did the math book look sad? Because it had too many problems!"])
    elif "coin flip" in text \
        or "flip a coin" in text \
        or "heads or tails" in text:
        coin = random.randint(0,1)
        if coin == 0:
            return "Heads"
        else:
            return "Tails"
    elif waiting_for_mood:
        waiting_for_mood = False
        if "good"in text \
            or "great" in text \
            or "awesome" in text:
            return "That's good to hear"
        else:
            return "Hope you get better :D"
    elif "how are you" in text:
        waiting_for_mood = True
        return "Good, how about you?"
    elif "what's my favorite game" in text or \
    "whats my favorite game" in text:
        return "Your favorite game is: " + favorite_game
    elif "do it"in text:
        return "no but, I can help you do it, but not do it for you"
    elif "homework" in text \
        or "help me with my homework" in text \
        or "help me with homework" in text:
        waiting_for_homework_subject = True
        return "What subject?"
    elif waiting_for_homework_subject:
        homework_subject = text
        waiting_for_homework_subject = False
        waiting_for_homework_topic = True
        return "And what topic in " + homework_subject + "?"
    elif waiting_for_homework_topic:
        waiting_for_homework_topic = False
        if "algebra" in text or \
            "biology" in text or \
            "world history" in text or \
            "grammar" in text or \
            "world war" in text:
            return text + "? I already have a study plan for that >:)"
        else:
            return "I don't have a study plan for that topic."
    elif "grade calculator" in text:
        grade_step = 1
        return "What is your math grade?"
    elif grade_step == 1:
        math_grade = int(text)
        grade_step = 2
        return "What is your science grade?"
    elif grade_step == 2:
        science_grade = int(text)
        grade_step = 3
        return "What is your history grade?"
    elif grade_step == 3:
        history_grade = int(text)
        grade_step = 4
        return "What is your english grade?"
    elif grade_step == 4:
        english_grade = int(text)
        grade_step = 0
        return "Your average grade is: " + str((math_grade + science_grade + history_grade + english_grade) / 4)

    else:
        return "My current capabilities don't allow me to answer this, try asking me something else, or type 'help' to see what I can do"
def send():
    text = entry.get().lower()
    add_message("You: " + text + "\n\n")
    response = vega_response(text)
    add_message("Vega: " + response + "\n\n")
    entry.delete(0, tk.END)
    entry.focus()
    if "bye" in text:
        add_message("Vega: Goodbye!\n\n")
        window.destroy()
        return

window = tk.Tk()

window.title("Vega Jr. V_0.9.0 Beta")
window.geometry("600x400")

chat = tk.Text(window, height=15, width=60, bg="black", fg="lime")
chat.pack(pady=10)
add_message("Vega: Hello I'm Vega Jr. ready to be your assistant! \n")
chat.see(tk.END)

entry = tk.Entry(window, width=40, bg="black", fg="white", insertbackground="white")
entry.pack(pady=10)
entry.bind("<Return>", lambda event: send())

button = tk.Button(window, text="send", bg="gray20", fg="white", command=send)
button.pack()

window.configure(bg="black")

window.mainloop()