from tkinter import filedialog
import customtkinter as ctk
from utils.GameScheduleManager import GameScheduleManager

# UI
root = ctk.CTk()
ctk.set_appearance_mode("dark")

root.geometry("750x450")
root.title("Game Schedule Extractor")

title_label = ctk.CTkLabel(root, text="Spiele exportieren", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

url_container = ctk.CTkFrame(master=root, height=100, width=350)
url_container.pack()

team_input = ctk.CTkEntry(url_container, placeholder_text="Team", width=300)
team_input.pack(padx=(10, 10), pady=(10, 0))

url_input = ctk.CTkEntry(url_container, placeholder_text="URL", width=300)
url_input.pack(padx=(10, 10), pady=(10, 0))

message_label = ctk.CTkLabel(root, text="Die ICS Datei wurde generiert!", text_color='green', font=ctk.CTkFont(size=20))
message_label.pack_forget()

def startExtractor():
    if team_input and url_input:
        # Disable message_label
        message_label.pack_forget()
        # Get Path for ICS Files
        root.directory = filedialog.askdirectory()

        # If Path is selected start GameSchedule Manager
        if root.directory:
            GameScheduleManager.getGamedays(url_input.get(), team_input.get(), root.directory)
            message_label.pack(padx=(0, 0), pady=(10, 0))
        else:
            print("Es wurde kein Ordner ausgewählt!")
    else:
        print("Es wurde kein Team und oder Url mit gegeben!")

url_button = ctk.CTkButton(url_container, text="Exportieren", command=startExtractor)
url_button.pack(pady=(10, 10))


if __name__ == '__main__':
    root.mainloop()
