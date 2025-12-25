


import customtkinter as ctk

def create_side_frame(parent):
    side_frame = ctk.CTkFrame(parent, width=150, border_width=1,
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

def create_dscm_frame(parent):
    # main_frame=ctk.CTkFrame(window,fg_color=window.cget('fg_color'))
    dscm_frame = ctk.CTkFrame(parent, fg_color='grey')

    # ---------- Labels + Textboxes Data ----------
    fields = [
        "FTTH No",
        "Name",
        "Contact No",
        "Bill Amount",
        "Cash Received",
        "Balance ",
        "Cash With",
        "Remarks"
    ]

    y_pos = 30

    for field in fields:
        lbl = ctk.CTkLabel(
            dscm_frame,
            text=field,
            font=("Arial", 15),
            text_color="white"
        )
        lbl.place(x=20, y=y_pos)

        
        # 🔹 ComboBox only for "Cash With"
        if field == "Cash With":
            widget = ctk.CTkComboBox(
                dscm_frame,
                width=200,
                values=["COUNTER", "IOB-ACCOUNT", "TEKNIX" , "BETA-ACCOUNT" ,"CUSTOMER" , "OTHERS"],
                fg_color="white",
                text_color="black",
                corner_radius=8
            )
        else:
            widget = ctk.CTkEntry(
                dscm_frame,
                width=200,
                fg_color="white",
                text_color="black",
                corner_radius=8
            )

        widget.place(x=180, y=y_pos)
        y_pos += 50  # move down for next field

    # ---------- Buttons: Save + Cancel ----------
    save_btn = ctk.CTkButton(
        dscm_frame,
        text="Save",
        width=100,
        fg_color="green",
        text_color="white",
    )
    save_btn.place(x=60, y=y_pos + 20)

    cancel_btn = ctk.CTkButton(
        dscm_frame,
        text="Cancel",
        width=100,
        fg_color="red",
        text_color="white",
    )
    cancel_btn.place(x=200, y=y_pos + 20)


    return dscm_frame