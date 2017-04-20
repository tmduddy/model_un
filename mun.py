import tkinter

window = tkinter.Tk()

window.title("Pitt Model UN")
#window.geometry("1200x900")

# arrays #
speakers_list = [""]
# end arrays #
# functions #
def add_to_speakers_list(name):
    speakers_list.append(name)

    for i in range(len(speakers_list)):
        speaker = tkinter.Label(window, text=str(speakers_list[i]))
        speaker.pack()


def remove_recent_speaker(name):
    speakers_list.pop()

# end functions #

# labels #
speak_label = tkinter.Label(window, text="Speaker's List")
# end labels #

# entry windows #
speak_enter = tkinter.Entry(window)
# end entry windows #

# buttons #
speak_submit = tkinter.Button(window, text="Add Speaker", command=lambda: add_to_speakers_list(speak_enter.get()))
# end buttons #


speak_label.pack()
speak_enter.pack(side=tkinter.LEFT)
speak_submit.pack(side=tkinter.LEFT)

#--- Draw Window ---#
window.mainloop()
