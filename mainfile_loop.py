import customtkinter as ctk
from dscm_frame import create_dscm_frame
from cbp_frame import create_cbp_frame

frames = {}

def show_frame(name, parent):
    # destroy existing frame if exists
    for frame in frames.values():
        frame.destroy()
    frames.clear()

    # create selected frame
    if name == "DSCM":
        frames["DSCM"] = create_dscm_frame(parent)
    elif name == "CBP":
        frames["CBP"] = create_cbp_frame(parent)

    # show frame
    frames[name].pack(side='left', fill='both', expand=True, padx=5, pady=5)



def create_side_frame(parent, main_parent):
    side_frame = ctk.CTkFrame(parent, width=200, border_width=1,
                              border_color='red', fg_color='coral1')

    side_frame_colour = side_frame.cget('fg_color')

    buttons = [
        ("DSCM BILL", 30, "DSCM"),
        ("CBP BILL", 130, "CBP"),
        ("CTOP-UP BILL", 230, "CTOP"),
        ("OTHER-COLLECTION", 330, "OTHER"),
        ("EXPENSE", 430, "EXPENSE"),
        ("STOCK PURCHASE", 530, "STOCK"),
    ]

    for text, y, key in buttons:
        btn = ctk.CTkButton(
            side_frame,
            text=text,
            text_color='white',
            font=('Bold', 15),
            width=60,
            hover=False,
            fg_color=side_frame_colour,
            command=lambda k=key: show_frame(k, main_parent)
        )
        btn.place(x=5 if y >= 330 else 10, y=y)

    return side_frame



if __name__ == '__main__':
    window = ctk.CTk()
    window.configure(fg_color="#1e90ff")
    window.title("One-Solution")
    window.geometry("800x800")
    window.iconbitmap("icon-Bharat BNET.ico")
    window.resizable(False, False)

    # side frame
    side_frame = create_side_frame(window, window)
    side_frame.pack(side='left', fill='y', padx=5, pady=5)

    # show default frame
    show_frame("DSCM", window)

    window.mainloop()
