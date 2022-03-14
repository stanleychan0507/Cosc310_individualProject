from tkinter import *
from chat import get_response, bot_name

BG_DIVIDER = "#2C2F33"
BG_COLOR = "#23272A"
TEXT_COLOR = "#99AAB5"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

root = Tk()

class ChatApplication:
    
    def __init__(self):
        self._setup_main_window()
        
    def run(self):
        root.mainloop()
        
    def _setup_main_window(self):
        root.title("Chat")
        root.resizable(width=False, height=False)
        root.configure(width=800, height=550, bg=BG_COLOR)
        
        # Head Label
        head_label = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Team1 Chat Bot", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # Text Display
        self.text_widget = Text(root, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
    
        # Bottom Div
        bottom_label = Label(root, bg=BG_DIVIDER, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # Message Entry
        self.msg_entry = Entry(bottom_label, bg="#2C2F33", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # Send Button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_DIVIDER, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()