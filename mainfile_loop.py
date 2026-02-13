import customtkinter as ctk
from dscm_frame import create_dscm_frame


def create_side_frame(parent):
    side_frame = ctk.CTkFrame(parent, width=200, border_width=1,
                              border_color='red', fg_color='coral1')

    side_frame_colour = side_frame.cget('fg_color')

    buttons = [
        ("DSCM BILL", 30),
        ("CBP BILL", 130),
        ("CTOP-UP BILL", 230),
        ("OTHER-COLLECTION", 330),
        ("EXPENSE", 430),
        ("STOCK PURCHASE", 530),
    ]

    for text, y in buttons:
        btn = ctk.CTkButton(
            side_frame,
            text=text,
            text_color='white',
            font=('Bold', 15),
            width=60,
            hover=False,
            fg_color=side_frame_colour
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

    # import sidebar
    side_frame = create_side_frame(window)
    side_frame.pack(side='left', fill='y', padx=5, pady=5)

    #main_frame
    dscm_frame= create_dscm_frame(window)
    dscm_frame.pack(side='left', fill='both', expand=True, pady=5, padx=5)



    window.mainloop()
