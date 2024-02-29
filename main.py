import time
from tkinter import filedialog
import customtkinter as ctk
from utils.GameScheduleManager import GameScheduleManager
import threading

# UI
root = ctk.CTk()
ctk.set_appearance_mode("dark")

root.geometry("750x450")
root.title("Game Schedule Extractor")

title_label = ctk.CTkLabel(root, text="Spiele exportieren", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

# Progressbar Widget erstellen
progressbar = ctk.CTkProgressBar(master=root, mode="indeterminate")
progressbar.pack(padx=20, pady=10)
progressbar.pack_forget()

url_container = ctk.CTkFrame(master=root, height=100, width=350)
url_container.pack()

team_input = ctk.CTkEntry(url_container, placeholder_text="Team", width=300)
team_input.pack(padx=(10, 10), pady=(10, 0))

url_input = ctk.CTkEntry(url_container, placeholder_text="URL", width=300)
url_input.pack(padx=(10, 10), pady=(10, 0))

message_label = ctk.CTkLabel(root, text="Die ICS Datei wurde generiert!", text_color='green', font=ctk.CTkFont(size=20))
message_label.pack_forget()

def startExtractor():
    if team_input.get() and url_input.get():  # Hier sollte .get() verwendet werden, um den Text zu erhalten
        # Disable message_label
        message_label.pack_forget()
        # Get Path for ICS Files
        root.directory = filedialog.askdirectory()

        if root.directory:
            def task():
                #ProgressBar starten
                progressbar.pack(padx=20, pady=10)
                progressbar.start()

                GameScheduleManager.generate_ICS_File(url_input.get(), team_input.get(), root.directory)

                # ProgressBar stoppen
                progressbar.stop()
                progressbar.pack_forget()

                # Aktualisiere UI nach Abschluss im Hauptthread
                message_label.pack(padx=(0, 0), pady=(10, 0))

            # Erstelle und starte den Thread
            thread = threading.Thread(target=task)
            thread.start()
        else:
            print("Es wurde kein Ordner ausgewählt!")
    else:
        print("Es wurde kein Team und/oder URL mitgegeben!")


url_button = ctk.CTkButton(url_container, text="Exportieren", command=startExtractor)
url_button.pack(pady=(10, 10))



# Funktion, um den Ladebalken zu aktualisieren
def start_loading():
    for i in range(100):
        # Aktualisiert den Wert der Progressbar
        progressbar['value'] = i
        root.update_idletasks()  # Aktualisiert die GUI
        time.sleep(0.05)  # Kurze Pause, um den Ladeeffekt zu simulieren

if __name__ == '__main__':
    root.mainloop()
