import tkinter as tk


class TypingTestApp:
    def __init__(self, r):
        self.root = r
        self.root.title("Typing test")
        self.sample_text_index = 0

        # Create label
        self.title_label = tk.Label(master=r, text="Typing Speed Test", font=("Arial", 50))
        self.title_label.pack(pady=10)

        self.desc_label = tk.Label(master=r,
                                   text="How fast are your fingers? Do the one-minute typing test to find out! \n "
                                        "Press the space bar after each word. \nAt the end, you'll get your typing "
                                        "speed in WPM. \nGood luck!",
                                   font=("Arial", 20))
        self.desc_label.pack(pady=10)

        self.score_label = tk.Label(master=r, text="Most recent score:", font=("Arial", 20))
        self.score_label.pack(pady=10)

        # Display the sample text
        self.sample_text_arr = ["Word processors evolved dramatically once they became software programs rather than "
                                "dedicated machines. They can usefully be distinguished from text editors, the "
                                "category of software they evolved from. Word processing added to the text editor "
                                "the ability to control type style and size, to manage lines (word wrap), "
                                "to format documents into pages, and to number pages. Functions now taken for "
                                "granted were added incrementally, sometimes by purchase of independent providers "
                                "of add-on programs. Spell checking, grammar checking and mail merge were some of "
                                "the most popular add-ons for early word processors. Word processors are also capable "
                                "of hyphenation, and the management and correct positioning of footnotes and endnotes. "
                                "Later desktop publishing programs were specifically designed with elaborate "
                                "pre-formatted layouts for publication, offering only limited options for changing "
                                "the layout, while allowing users to import text that "
                                "was written using a text editor or word processor, or type the text in themselves.",
                                "The Master of Business Administration (MBA or M.B.A.) degree originated in the United "
                                "States in the early 20th century when the country industrialized and companies sought "
                                "scientific approaches to management. The core courses in an MBA program cover various "
                                "areas of business such as accounting, applied statistics, business communication, "
                                "business ethics, business law, finance, managerial economics, management, "
                                "entrepreneurship, marketing and operations in a manner most relevant to management "
                                "analysis and strategy. Most programs also include elective courses and concentrations "
                                "for further study in a particular area, for example accounting, finance, and "
                                "marketing. MBA programs in the United States typically require completing about "
                                "sixty credits, nearly twice the number of credits typically required for degrees "
                                "that cover some of the same material such as the Master of Economics, Master of "
                                "Finance, Master of Accountancy, Master of Science in Marketing and Master of Science "
                                "in Management, The MBA is a terminal degree and a professional degree. Accreditation "
                                "bodies specifically for MBA programs ensure consistency and quality of education. "
                                "Business schools in many countries offer programs tailored to full-time, part-time, "
                                "executive (abridged coursework typically occurring on nights or weekends) and "
                                "distance learning students, many with specialized concentrations.",
                                "Trying to make a wise, good choice when thinking about what kinds of careers might be "
                                "best for you is a hard thing to do. Your future may very well depend on the ways you "
                                "go about finding the best job openings for you in the world of work. Some people will "
                                "feel that there is one and only one job in the world for them. Hard thinking and a "
                                "lot of hard work will help them find the one job that is best for them. Jobs are "
                                "there for those with skills and a good work ethic. Many new young artists in the upper"
                                " New England states are famous around the world as leaders in new American art. "
                                "These fine artists are very good in their chosen fields and are willing to share "
                                "their many talents by teaching others. The students have had the chance to learn "
                                "and use skills in oil painting, sketching with chalk, sculpting, and weaving. "
                                "Learning to typewrite is a skill that will help all of us in our work today. The "
                                "development of the computer will open doors for people with the keyboarding skills "
                                "and will make typing a necessity. Managers, as well as secretaries, will need skill "
                                "at the keyboard to input data and process words. Therefore, good keyboarding skills "
                                "may be important to you."]

        self.sample_label = tk.Label(r, text=self.sample_text_arr[self.sample_text_index], wraplength=400,
                                     justify="left")
        self.sample_label.pack(pady=10)

        # Entry widget for user to type the text
        self.entry = tk.Entry(r, width=50)
        self.entry.pack(pady=10)

        # Button to start the test
        self.start_button = tk.Button(r, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)

    def start_test(self):
        # Clear previous results
        self.entry.delete(0, tk.END)
        self.start_button.destroy()

        # Create a countdown timer for 1 minute
        countdown_timer = CountdownTimer(r=self.root, a=self, duration=60)
        countdown_timer.start_countdown()

    def calculate_wpm(self, typed_text, elapsed_time):
        words = len(typed_text.split())
        minutes = elapsed_time / 60
        return words / minutes

    def calculate_accuracy(self, typed_text, sample_text):
        if len(typed_text) == 0:
            return 0
        correct_chars = sum(1 for a, b in zip(typed_text, sample_text) if a == b)
        total_chars = len(typed_text)
        return (correct_chars / total_chars) * 100


class CountdownTimer:
    def __init__(self, r, a, duration):
        self.root = r
        self.duration = duration
        self.time_left = duration
        self.app = a

        # Label to display the countdown time
        self.label = tk.Label(r, text=self.format_time(self.time_left), font=("Helvetica", 48))
        self.label.pack(pady=20)

    def format_time(self, seconds):
        return f"{seconds} seconds"

    def start_countdown(self):
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            if self.label:
                self.label.config(text=self.format_time(self.time_left))
            self.root.after(1000, self.update_timer)
        else:
            if self.label:
                self.label.config(text="Time's up!")
                self.label.destroy()
            # Calculate typing speed and accuracy
            typed_text = self.app.entry.get()
            wpm = self.app.calculate_wpm(typed_text, 60)
            accuracy = self.app.calculate_accuracy(typed_text, self.app.sample_text_arr[self.app.sample_text_index])

            # Display the results
            result_text = f"Most recent score: WPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%"
            self.app.score_label.config(text=result_text)
            self.app.entry.delete(0, tk.END)

            # Button to start the test
            self.app.start_button = tk.Button(self.root, text="Start Test", command=self.app.start_test)
            self.app.start_button.pack(pady=10)

            # Display the sample text
            self.app.sample_text_index = (self.app.sample_text_index + 1) % len(self.app.sample_text_arr)
            self.app.sample_label.config(text=self.app.sample_text_arr[self.app.sample_text_index])


# Create root window
root = tk.Tk()
app = TypingTestApp(root)

root.mainloop()
