import tkinter as tk
from tkinter import messagebox
default_font = ("Arial", 20, "bold")

window = tk.Tk()
window.geometry("500x700")
window.title("My Music Preferences")

window.iconbitmap(r".\images\note.ico")

title = tk.Label(window,
                 font=default_font,
                 text="Welcome to My Music Preferences!",
                 foreground="purple"
                 )
title.pack()

entry_title = tk.Label(window,
                       font=("Arial", 15),
                       text="Who is your favorite artist or band?",
                       pady=30
                       )
entry_title.pack()

entry = tk.Entry(window,
                 width=25
                 )
entry.pack()

music_genres_title = tk.Label(window,
                              font=("Arial", 15),
                              text="Select your favorite music genres:",
                              pady=30
                              )
music_genres_title.pack()

check_rock = tk.IntVar()
check_pop = tk.IntVar()
check_jazz = tk.IntVar()


genre_rock_checkbox = tk.Checkbutton(window,
                                      font=("Arial", 15),
                                      text="Rock",
                                      variable=check_rock
                                      )
genre_rock_checkbox.pack(anchor="w")

genre_pop_checkbox = tk.Checkbutton(window,
                                     font=("Arial", 15),
                                     text="Pop",
                                     variable=check_pop
                                     )
genre_pop_checkbox.pack(anchor="w")

genre_jazz_checkbox = tk.Checkbutton(window,
                                      font=("Arial", 15),
                                      text="Jazz",
                                      variable=check_jazz
                                      )
genre_jazz_checkbox.pack(anchor="w")

method = tk.StringVar(value="Something")

choose_pref_method_title = tk.Label(window,
                                    font=("Arial", 15),
                                    text="Choose your preferred listening method:",
                                    pady=30
                                    )
choose_pref_method_title.pack()

method_streaming_mark = tk.Radiobutton(window,
                                           font=("Arial", 15),
                                           text="Streaming",
                                           var=method,
                                           val="Streaming"
                                           )

method_cds_mark = tk.Radiobutton(window,
                                     font=("Arial", 15),
                                     text="CDs",
                                     var=method,
                                     val="CDs"
                                     )

method_vinyl_mark = tk.Radiobutton(window,
                                       font=("Arial", 15),
                                       text="Vinyl",
                                       var=method,
                                       val="Vinyl"
                                       )

method_streaming_mark.pack(anchor="w")
method_cds_mark.pack(anchor="w")
method_vinyl_mark.pack(anchor="w")

def submit_btn():
    favorite_artist_data = entry.get()
    genres = []
    if check_rock.get():
        genres.append("Rock")
    if check_pop.get():
        genres.append("Pop")
    if check_jazz.get():
        genres.append("Jazz")
    listening_method = method.get()

    # Prepare data for the messagebox
    genres_text = ", ".join(genres) if genres else "None"
    messagebox.showinfo("Music Preferences",
                        f"Favorite Artist/Band: {favorite_artist_data}\n"
                        f"Favorite Genres: {genres_text}\n"
                        f"Preferred Listening Method: {listening_method}")

submit = tk.Button(window,
                   font=("Arial", 15),
                   text="Submit",
                   bg="blue",
                   fg="white",
                   command=submit_btn
                   )
submit.pack()



window.mainloop()

