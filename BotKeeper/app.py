import threading
from tkinter import *
from chat import get_response, bot_name
from scheduler import Scheduler

BG_GRAY = "#ABB289"
BG_COLOUR = "#17202A"
TEXT_COLOUR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    def __init__(self):
        print("Chat Application instance created.")
        self.window = Tk()
        self._setup_main_window()
        self.scheduler = Scheduler()
        self.scheduler_thread = None

    def run(self):
        print("Mainloop started")
        self.start_scheduler()
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOUR)

        head_label = Label(self.window, bg=BG_COLOUR, fg=TEXT_COLOUR, text="BotKeeper - A chatbot shop owner", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOUR, fg=TEXT_COLOUR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOUR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You: ")

        def delayed_response(msg):
            response = get_response(msg)
            self._insert_message(response, f"{bot_name}: ")

        self.scheduler.schedule_task(3, delayed_response, (msg,))

    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}{msg}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        self.text_widget.see(END)

    def start_scheduler(self):
        if not self.scheduler_thread or not self.scheduler_thread.is_alive():
            self.scheduler_thread = threading.Thread(target=self.scheduler.run)
            self.scheduler_thread.start()
            print("Scheduler thread started")

    def stop_scheduler(self):
        self.scheduler.cancel_all_tasks()
        if self.scheduler_thread and self.scheduler_thread.is_alive():
            self.scheduler_thread.join()
            self.scheduler_thread = None
            print("Scheduler thread stopped")

    def __del__(self):
        self.stop_scheduler()

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
