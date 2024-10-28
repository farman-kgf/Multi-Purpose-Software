import datetime
import pywhatkit as kit
import customtkinter as ctk
from tkinter import messagebox
from tabulate import tabulate
import random as r

# Initialize CustomTkinter
ctk.set_appearance_mode("Dark")  # Dark theme
ctk.set_default_color_theme("blue")  # Green theme

# Function to run the selected application
def run_selected_app(app_number):
    if app_number == 1:
        run_attendance_system()
    elif app_number == 2:
        run_bank_management_game()
    elif app_number == 3:
        run_counseling_chatbot()
    elif app_number == 4:
        run_rock_paper_scissors()
    elif app_number == 5:
        run_number_guessing_game()
    elif app_number == 6:
        run_calculator()
    elif app_number == 7:
        sumesh_program()

# Main function to create the mobile-like interface
def main():
    root = ctk.CTk()  # Main window
    root.title("Multi-Purpose Softwere")
    root.geometry("350x600")  # Mobile-sized window
    root.resizable(False, False)  # Prevent resizing

    # Create a title label
    title_label = ctk.CTkLabel(master=root, text="Multi-Purpose App", font=("Arial", 24))
    title_label.pack(pady=20)

    # Create buttons for each application
    app_buttons = [
        ("Attendance System", 1),
        ("Bank Management Game", 2),
        ("Counseling Chatbot", 3),
        ("Rock-Paper-Scissors", 4),
        ("Number Guessing Game", 5),
        ("Calculator", 6),
        ("sumesh project", 7)
    ]

    for app_name, app_number in app_buttons:
        button = ctk.CTkButton(master=root, text=app_name, command=lambda num=app_number: run_selected_app(num), width=250)
        button.pack(pady=10)

    # Run the application
    root.mainloop()

# Function stubs for each application (replace with actual implementations)
def run_attendance_system():
    def get_student_data():
        return [
            ("Manisha Borah", "g"),
            ("Rupali Jonak Mahanta", "g"), 
            ("Sakshi Satish Kohle", "g"),
            ("Abhinav Anubhab Khound", "b"), 
            ("Bibhuti Ranjan Borah", "b"), 
            ("Himanshu Gupta", "b"),
            ("Mohd. Farman Usta", "b"), 
            ("Prasujya Pritam Borah", "b"), 
            ("Vansh Behal", "b"),
            ("Anamika Das", "g"), 
            ("Aryan Raj Gupta", "b"), 
            ("Bhagyashree Saikia", "g"),
            ("Bhumika Roy", "g"), 
            ("Bhumika Sarma", "g"), 
            ("Bonani Bhuyan", "g"),
            ("Bedangraj Baruah", "b"), 
            ("Deepanita Chakraborty", "g"), 
            ("Geetashree Baruah", "g"),
            ("Hemphu Engti", "b"), 
            ("Himashree Nag", "g"), 
            ("Himesh Biswas", "b"),
            ("Himanku Rajkhown", "b"), 
            ("Manyataa Kashyap", "g"), 
            ("Mouchami Nath", "g"),
            ("Prakiti Bora", "g"), 
            ("Priyam Bora", "b"), 
            ("Priyanko Devchoudhary", "b"),
            ("Rituparna Deka", "g"), 
            ("Rupjyoti Borah", "b"), 
            ("Suprabhat Borah", "b"),
            ("Uday Debnath", "b"), 
            ("Kumari Lucky", "g"), 
            ("Tulika Singhal", "g"),
            ("Sumesh Kumar", "b"), 
            ("Debasish Borah", "b")
        ]

    # Function to validate password
    def get_password():
        valid_passwords = [12345, "12345"]
        password = ctk.CTkInputDialog(text="Enter the password:", title="Password").get_input()
        if password and int(password) in valid_passwords:
            return True
        else:
            messagebox.showerror("Error", "Invalid password.")
            return False

    # Function to collect attendance using dropdown selection
    def collect_attendance(students):
        attendance = {}
        present_count = 0
        absent_students = []

        # Create attendance window for input
        attendance_window = ctk.CTkToplevel()
        attendance_window.title("e-Attendance")
        attendance_window.geometry("450x600")

        # Create a scrollable frame for the attendance list
        scrollable_frame = ctk.CTkScrollableFrame(master=attendance_window, width=400, height=500, corner_radius=10)
        scrollable_frame.pack(pady=20, padx=10, fill="both", expand=True)

        # Create a dictionary to store the attendance status of each student
        status_options = {}

        # Loop through each student to create options for attendance
        for idx, (name, gender) in enumerate(students, start=1):
            g_b = "GIRL" if gender == "g" else "BOY"

            # Create a label for each student
            student_label = ctk.CTkLabel(scrollable_frame, text=f"{idx}. {name} ({g_b})", font=("Arial", 12))
            student_label.pack(pady=5)

            # Create an OptionMenu for present/absent
            options = ["Present", "Absent"]
            status_options[name] = ctk.StringVar(value="Present")
            attendance_menu = ctk.CTkOptionMenu(scrollable_frame, variable=status_options[name], values=options)
            attendance_menu.pack(pady=5)

        # Create a function to collect attendance status
        def submit_attendance():
            nonlocal present_count, absent_students

            # Loop through the status options and update attendance
            for idx, (name, gender) in enumerate(students, start=1):
                g_b = "GIRL" if gender == "g" else "BOY"
                status = status_options[name].get()

                if status == "Present":
                    present_count += 1
                    attendance[idx] = [name, "PRESENT", g_b]
                else:
                    absent_students.append(name)
                    attendance[idx] = [name, "ABSENT", g_b]

            attendance_window.destroy()  # Close the attendance window after submission

        # Create a submit button
        submit_button = ctk.CTkButton(attendance_window, text="Submit Attendance", command=submit_attendance)
        submit_button.pack(pady=10)

        attendance_window.mainloop()  # Run the attendance window

        return attendance, present_count, absent_students

    # Function to save attendance to a file
    def save_to_file(filename, attendance, present_count, total_students, absent_students):
        with open(filename, 'w') as f:
            current_time = datetime.datetime.now()
            f.write(f"Total number of students: {total_students}\n")
            f.write(f"At Date and Time from timestamp: {current_time}\n")
            
            # Attendance Table
            headers = ['NAME', 'STATUS', 'GENDER']
            table = [[data[0], data[1], data[2]] for data in attendance.values()]
            f.write(tabulate(table, headers, tablefmt='grid') + "\n")

            # Absent Students
            f.write("Students who are absent:\n")
            f.write("\n".join(absent_students) + "\n")
            
            f.write(f"Total number of students present: {present_count}\n")
            f.write(f"Total number of students absent: {total_students - present_count}\n")
            f.write(f"Total girls: {sum(1 for _, _, g in attendance.values() if g == 'GIRL')}\n")
            f.write(f"Total boys: {sum(1 for _, _, g in attendance.values() if g == 'BOY')}\n")

    # Function to send WhatsApp message
    def send_whatsapp_message(phone_number, message, hour, minute):
        kit.sendwhatmsg(phone_number, message, hour, minute)

    # Main function to run the attendance system
    def main():
        if get_password():
            filename = ctk.CTkInputDialog(text="Enter the filename to save (add .txt at the end):", title="Filename").get_input()
            if filename:
                students = get_student_data()
                attendance, present_count, absent_students = collect_attendance(students)
                total_students = len(students)

                # Save attendance data to file
                save_to_file(filename, attendance, present_count, total_students, absent_students)

                # Create message with attendance summary
                absent_list = "\n".join(absent_students)
                message = (f"Attendance Report Saved.\n"
                        f"Total Students: {total_students}\n"
                        f"Total Present: {present_count}\n"
                        f"Total Absent: {total_students - present_count}\n"
                        f"Absent Students:\n{absent_list}")

                # Specify the time to send the message
                now = datetime.datetime.now()
                send_hour = now.hour
                send_minute = now.minute + 2

                # Adjust minute and hour if minute exceeds 59
                if send_minute >= 60:
                    send_minute -= 60
                    send_hour += 1

                # Send WhatsApp message at the specified time
                send_whatsapp_message("+918399925675", message, send_hour, send_minute)
                messagebox.showinfo("Success", "Attendance recorded and WhatsApp message sent!")

    # Set up the main customtkinter window
    ctk.set_appearance_mode("Dark")  # Dark theme for a modern look
    ctk.set_default_color_theme("green")  # Green theme for visual appeal

    root = ctk.CTk()  # Use CTk instead of Tk
    root.title("KV MISA Attendance System")
    root.geometry("500x300")

    # Create a frame for better layout
    frame = ctk.CTkFrame(master=root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title Label
    title_label = ctk.CTkLabel(master=frame, text="KV MISA Attendance System", font=("Arial", 24))
    title_label.pack(pady=10)

    # Add a separator line for design
    separator = ctk.CTkLabel(master=frame, text="--------------------", font=("Arial", 14))
    separator.pack()

    # Instructions Label
    instructions_label = ctk.CTkLabel(master=frame, text="Click the button below to start attendance:", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Start Attendance Button
    start_button = ctk.CTkButton(master=frame, text="Start Attendance", command=main, corner_radius=8, width=200)
    start_button.pack(pady=20)

    # Footer Label
    footer_label = ctk.CTkLabel(master=frame, text="Made by Farman & Himanshu", font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    root.mainloop()

def run_bank_management_game():
    # Initialize the application
    ctk.set_appearance_mode("Dark")  # Modes: "Dark"
    ctk.set_default_color_theme("blue")

    class BankApp(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.title("Simple Bank Management Game")
            self.geometry("400x400")
            
            self.credit = 0
            self.remaining_amount = 0
            self.spending_count = 0
            
            self.create_widgets()

        def create_widgets(self):
            self.label_title = ctk.CTkLabel(self, text="Welcome to the Bank Management Game")
            self.label_title.pack(pady=10)

            self.entry_name = ctk.CTkEntry(self, placeholder_text="Enter your name")
            self.entry_name.pack(pady=5)

            self.entry_credit = ctk.CTkEntry(self, placeholder_text="Enter amount to credit")
            self.entry_credit.pack(pady=5)

            self.button_credit = ctk.CTkButton(self, text="Credit Money", command=self.credit_money)
            self.button_credit.pack(pady=10)

            self.label_spend = ctk.CTkLabel(self, text="")
            self.label_spend.pack(pady=5)

        def credit_money(self):
            self.credit = float(self.entry_credit.get())
            
            if self.credit < 5:
                messagebox.showwarning("Warning", "You have to put at least $5")
                return
            
            self.remaining_amount = self.credit
            self.label_spend.configure(text="Amount credited: ${:.2f}".format(self.credit))
            self.entry_credit.delete(0, 'end')

            self.ask_spending()

        def ask_spending(self):
            if self.spending_count < 3:
                spending_amount = ctk.CTkEntry(self, placeholder_text=f"Enter amount to spend (Transaction {self.spending_count + 1})")
                spending_amount.pack(pady=5)

                spend_button = ctk.CTkButton(self, text="Spend Money", command=lambda: self.spend_money(spending_amount))
                spend_button.pack(pady=10)

        def spend_money(self, spending_amount_entry):
            spending_amount = float(spending_amount_entry.get())
            self.remaining_amount -= spending_amount
            self.spending_count += 1
            
            if self.remaining_amount > 0:
                messagebox.showinfo("Success", f"Transaction successful! Amount left: ${self.remaining_amount:.2f}")
                self.ask_spending()
            elif self.remaining_amount == 0:
                messagebox.showinfo("Win", "You win! Thanks for playing!")
                self.reset_game()
            else:
                messagebox.showwarning("Warning", "Insufficient funds! You spent more than available.")
                self.reset_game()

        def reset_game(self):
            self.credit = 0
            self.remaining_amount = 0
            self.spending_count = 0
            self.entry_name.delete(0, 'end')
            self.label_spend.configure(text="")
            for widget in self.winfo_children():
                if isinstance(widget, ctk.CTkEntry) and widget != self.entry_name:
                    widget.destroy()
            self.entry_credit.delete(0, 'end')

    # Run the application
    if __name__ == "__main__":
        app = BankApp()
        app.mainloop()

def run_counseling_chatbot():
    # Initialize the application
    ctk.set_appearance_mode("Dark")  # Modes: "Dark"
    ctk.set_default_color_theme("blue")  

    class CounselingChatbot:
        def __init__(self, root):
            self.root = root
            self.root.title("Counseling Chat Bot")
            self.count = 0
            self.questions = [
                "Do you feel motivated to attend school every day?",
                "Are you able to concentrate well during class?",
                "Do you feel comfortable sharing your thoughts with your teachers?",
                "Have you been sleeping well lately?",
                "Do you often feel anxious about your academic performance?",
                "Are you satisfied with your current social relationships at school?",
                "Do you find it easy to manage stress?",
                "Do you feel supported by your family in your studies?",
                "Have you felt overwhelmed by schoolwork recently?",
                "Do you feel confident in achieving your goals?"
            ]
            self.answers = []

            # Create UI components
            self.label = ctk.CTkLabel(root, text="Welcome to the Counseling Chat Bot\nAnswer in 'yes' or 'no'", font=("Arial", 16))
            self.label.pack(pady=10)

            self.question_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
            self.question_label.pack(pady=10)

            self.entry = ctk.CTkEntry(root, width=300)
            self.entry.pack(pady=10)

            self.submit_button = ctk.CTkButton(root, text="Submit", command=self.submit_answer)
            self.submit_button.pack(pady=10)

            self.result_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
            self.result_label.pack(pady=10)

            self.current_question_index = 0
            self.show_question()

        def show_question(self):
            if self.current_question_index < len(self.questions):
                self.question_label.configure(text=f"Q{self.current_question_index + 1}: {self.questions[self.current_question_index]}")
                self.entry.delete(0, ctk.END)
            else:
                self.evaluate_results()

        def submit_answer(self):
            answer = self.entry.get().strip().lower()
            if answer == "yes":
                self.count += 2
            elif answer == "no":
                if self.current_question_index in [4, 8]:  # Q5 and Q9
                    self.count += 2

            self.current_question_index += 1
            self.show_question()

        def evaluate_results(self):
            if self.count == 16:
                result = "YOU HAVE Mentally balanced and motivated."
            elif 16 > self.count > 9:
                result = "YOU HAVE Some areas of concern, but overall balanced."
            elif 10 > self.count > 4:
                result = "YOU HAVE Signs of stress or emotional imbalance."
            elif 5 > self.count > 0:
                result = "YOU HAVE High risk of mental or emotional strain; immediate counseling may be needed."
            else:
                result = "404 something went wrong."
            
            self.result_label.configure(text=f"{result} Score: {self.count}")

    root = ctk.CTk()  # Create a new window for the chatbot
    app = CounselingChatbot(root)
    root.mainloop()

if __name__ == "__main__":
    main()


def run_rock_paper_scissors():
    # Initialize CustomTkinter
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    class RockPaperScissors:
        def __init__(self, root):
            self.root = root
            self.root.title("Rock Paper Scissors")

            # Game state variables
            self.user_score = 0
            self.computer_score = 0
            self.rounds = 3
            self.current_round = 0

            # Create UI components
            self.label_title = ctk.CTkLabel(root, text="Rock Paper Scissors Game", font=("Arial", 24))
            self.label_title.pack(pady=10)

            self.label_score = ctk.CTkLabel(root, text="Your Score: 0 | Computer Score: 0", font=("Arial", 16))
            self.label_score.pack(pady=10)

            self.label_choice = ctk.CTkLabel(root, text="Choose your move:", font=("Arial", 16))
            self.label_choice.pack(pady=10)

            self.button_rock = ctk.CTkButton(root, text="Rock", command=lambda: self.play(1))
            self.button_rock.pack(side="left", padx=10, pady=10)

            self.button_paper = ctk.CTkButton(root, text="Paper", command=lambda: self.play(2))
            self.button_paper.pack(side="left", padx=10, pady=10)

            self.button_scissors = ctk.CTkButton(root, text="Scissors", command=lambda: self.play(3))
            self.button_scissors.pack(side="left", padx=10, pady=10)

            self.label_result = ctk.CTkLabel(root, text="", font=("Arial", 16))
            self.label_result.pack(pady=10)

            self.button_restart = ctk.CTkButton(root, text="Play Again", command=self.restart_game)
            self.button_restart.pack(pady=10)

            self.restart_game()

        def play(self, user_input):
            computer_guess = r.randint(1, 3)
            computer_choice = self.get_choice(computer_guess)
            user_choice = self.get_choice(user_input)

            self.label_result.configure(text=f"Computer chose: {computer_choice}\nYou chose: {user_choice}")

            if computer_guess == user_input:
                self.label_result.configure(text=self.label_result.cget("text") + "\nDraw!")
            elif (computer_guess == 1 and user_input == 2) or (computer_guess == 2 and user_input == 3) or (computer_guess == 3 and user_input == 1):
                self.user_score += 1
                self.label_result.configure(text=self.label_result.cget("text") + "\nYou won this round!")
            else:
                self.computer_score += 1
                self.label_result.configure(text=self.label_result.cget("text") + "\nComputer won this round!")

            self.current_round += 1
            self.update_score()

            if self.current_round >= self.rounds:
                self.end_game()

        def get_choice(self, choice_number):
            if choice_number == 1:
                return "Rock"
            elif choice_number == 2:
                return "Paper"
            elif choice_number == 3:
                return "Scissors"
            return "Invalid Choice"

        def update_score(self):
            self.label_score.configure(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")

        def end_game(self):
            if self.user_score > self.computer_score:
                result_text = "You won the game!"
            elif self.user_score < self.computer_score:
                result_text = "You lost the game!"
            else:
                result_text = "It's a draw!"

            self.label_result.configure(text=f"{self.label_result.cget('text')}\nGame Over! {result_text}")

            # Disable buttons after game over
            self.button_rock.configure(state="disabled")
            self.button_paper.configure(state="disabled")
            self.button_scissors.configure(state="disabled")

        def restart_game(self):
            self.user_score = 0
            self.computer_score = 0
            self.current_round = 0
            self.update_score()
            self.label_result.configure(text="")
            self.button_rock.configure(state="normal")
            self.button_paper.configure(state="normal")
            self.button_scissors.configure(state="normal")

    if __name__ == "__main__":
        root = ctk.CTk()
        app = RockPaperScissors(root)
        root.mainloop()
def run_number_guessing_game():
    # Initialize CustomTkinter
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    class NumberGuessingGame:
        def __init__(self, root):
            self.root = root
            self.root.title("Number Guessing Game")

            # Game state variables
            self.low = 1
            self.high = 100
            self.tries = 0
            self.guessed = False

            # Create UI components
            self.label_title = ctk.CTkLabel(root, text="Welcome to the Number Guessing Game!", font=("Arial", 24))
            self.label_title.pack(pady=10)

            self.label_instruction = ctk.CTkLabel(root, text="Think of a number between 1 and 100.", font=("Arial", 16))
            self.label_instruction.pack(pady=10)

            self.button_start = ctk.CTkButton(root, text="Start Game", command=self.start_game)
            self.button_start.pack(pady=10)

            self.label_guess = ctk.CTkLabel(root, text="", font=("Arial", 16))
            self.label_guess.pack(pady=10)

            self.entry_feedback = ctk.CTkEntry(root, width=300)
            self.entry_feedback.pack(pady=10)

            self.button_submit = ctk.CTkButton(root, text="Submit Feedback", command=self.submit_feedback)
            self.button_submit.pack(pady=10)

            self.label_result = ctk.CTkLabel(root, text="", font=("Arial", 16))
            self.label_result.pack(pady=10)

            self.reset_game()

        def reset_game(self):
            self.low = 1
            self.high = 100
            self.tries = 0
            self.guessed = False
            self.label_guess.configure(text="")
            self.label_result.configure(text="")
            self.entry_feedback.delete(0, ctk.END)
            self.button_start.configure(state="normal")

        def start_game(self):
            self.guess_number()

        def guess_number(self):
            if not self.guessed:
                self.guess = r.randint(self.low, self.high)
                self.label_guess.configure(text=f"I guess {self.guess}.")
                self.tries += 1
                self.entry_feedback.delete(0, ctk.END)
                self.entry_feedback.focus()

        def submit_feedback(self):
            feedback = self.entry_feedback.get().upper()
            if feedback == "C":
                self.label_result.configure(text=f"I guessed it in {self.tries} tries!")
                self.guessed = True
                self.button_start.configure(state="normal")
            elif feedback == "H":
                self.high = self.guess - 1
                self.guess_number()
            elif feedback == "L":
                self.low = self.guess + 1
                self.guess_number()
            else:
                self.label_result.configure(text="Invalid input. Please enter H, L, or C.")

    if __name__ == "__main__":
        root = ctk.CTk()
        app = NumberGuessingGame(root)
        root.mainloop()


def run_calculator():
    # Initialize the application
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    class Calculator:
        def __init__(self, root):
            self.root = root
            self.root.title("Simple Calculator")

            # Create UI components
            self.label_title = ctk.CTkLabel(root, text="Simple Calculator", font=("Arial", 24))
            self.label_title.pack(pady=10)

            self.label_instruction = ctk.CTkLabel(root, text="Enter two numbers and choose an operation:", font=("Arial", 16))
            self.label_instruction.pack(pady=10)

            self.entry_num1 = ctk.CTkEntry(root, placeholder_text="Input Number 1")
            self.entry_num1.pack(pady=5)

            self.entry_num2 = ctk.CTkEntry(root, placeholder_text="Input Number 2")
            self.entry_num2.pack(pady=5)

            self.label_result = ctk.CTkLabel(root, text="", font=("Arial", 16))
            self.label_result.pack(pady=10)

            self.button_add = ctk.CTkButton(root, text="+", command=lambda: self.calculate("+"))
            self.button_add.pack(side="left", padx=10)

            self.button_subtract = ctk.CTkButton(root, text="-", command=lambda: self.calculate("-"))
            self.button_subtract.pack(side="left", padx=10)

            self.button_multiply = ctk.CTkButton(root, text="*", command=lambda: self.calculate("*"))
            self.button_multiply.pack(side="left", padx=10)

            self.button_divide = ctk.CTkButton(root, text="/", command=lambda: self.calculate("/"))
            self.button_divide.pack(side="left", padx=10)

            self.button_power = ctk.CTkButton(root, text="**", command=lambda: self.calculate("**"))
            self.button_power.pack(side="left", padx=10)

            self.button_root = ctk.CTkButton(root, text="//", command=lambda: self.calculate("//"))
            self.button_root.pack(side="left", padx=10)

        def calculate(self, operation):
            try:
                num1 = float(self.entry_num1.get())
                num2 = float(self.entry_num2.get())

                if operation == "+":
                    result = num1 + num2
                elif operation == "-":
                    result = num1 - num2
                elif operation == "*":
                    result = num1 * num2
                elif operation == "/":
                    result = num1 / num2
                elif operation == "**":
                    result = num1 ** num2
                elif operation == "//":
                    result = num1 // num2

                self.label_result.configure(text=f"Result: {result}")
            except ValueError:
                self.label_result.configure(text="Invalid input. Please enter numbers.")
            except ZeroDivisionError:
                self.label_result.configure(text="Error: Division by zero.")

    if __name__ == "__main__":
        root = ctk.CTk()
        app = Calculator(root)
        root.mainloop()


def sumesh_program():
    print("phscale")

if __name__ == "__main__":
    main()