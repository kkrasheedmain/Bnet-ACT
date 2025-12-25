


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

def create_main_frame(parent):
    # main_frame=ctk.CTkFrame(window,fg_color=window.cget('fg_color'))
    main_frame = ctk.CTkFrame(parent, fg_color='grey')

    # ---------- Labels + Textboxes Data ----------
    fields = [
        "FTTH No",
        "Name",
        "Bill Amount",
        "Cash Received",
        "Balance To Customer",
        "Balance Pending",
        "Cash With",
        "Remarks"
    ]

    y_pos = 30

    for field in fields:
        lbl = ctk.CTkLabel(
            main_frame,
            text=field,
            font=("Arial", 15),
            text_color="white"
        )
        lbl.place(x=20, y=y_pos)

        ent = ctk.CTkEntry(
            main_frame,
            width=200,
            fg_color="white",
            text_color="black",
            corner_radius=8
        )
        ent.place(x=180, y=y_pos)

        y_pos += 50  # move down for next field

    # ---------- Buttons: Save + Cancel ----------
    save_btn = ctk.CTkButton(
        main_frame,
        text="Save",
        width=100,
        fg_color="green",
        text_color="white",
    )
    save_btn.place(x=60, y=y_pos + 20)

    cancel_btn = ctk.CTkButton(
        main_frame,
        text="Cancel",
        width=100,
        fg_color="red",
        text_color="white",
    )
    cancel_btn.place(x=200, y=y_pos + 20)


    return main_frame