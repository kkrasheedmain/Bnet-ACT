


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

###########################
def create_dscm_frame(parent):
    dscm_frame = ctk.CTkFrame(parent, fg_color='grey')
    dscm_frame.place(relwidth=1, relheight=1)

    fields = [
        "FTTH No",
        "Name",
        "Contact No",
        "Bill Amount",
        "Cash Received",
        "Balance",
        "Cash With",
        "Remarks"
    ]

    entries = {}
    ###############################################
    # ---------- FTTH VALIDATION ----------
    def validate_ftth(new_value):
        if new_value == "":
            return True

        # Only digits allowed
        if not new_value.isdigit():
            return False

        # Maximum 10 digits
        if len(new_value) > 10:
            return False

        # First digit must be 4 only
        if len(new_value) == 1 and new_value != "4":
            return False

        # Extra safety (if pasted full number)
        if len(new_value) > 1 and new_value[0] != "4":
            return False

        # Auto move to Name field after 10 digits
        if len(new_value) == 10:
            dscm_frame.after(10, lambda: entries["Name"].focus())

        return True

    # ---------- CONTACT VALIDATION ----------
    def validate_contact(new_value):
        if new_value == "":
            return True

        # Only digits allowed
        if not new_value.isdigit():
            return False

        # Maximum 10 digits
        if len(new_value) > 10:
            return False

        # First digit must be 6,7,8,9 only
        if len(new_value) == 1 and new_value not in ["6", "7", "8", "9"]:
            return False

        # Extra safety (if pasted full number)
        if len(new_value) > 1 and new_value[0] not in ["6", "7", "8", "9"]:
            return False

        # Auto move to Bill Amount after 10 digits
        if len(new_value) == 10:
            dscm_frame.after(10, lambda: entries["Bill Amount"].focus())

        return True


    # ---------- AMOUNT VALIDATION ----------
    def validate_amount(new_value):
        if new_value == "":
            return True

        try:
            float(new_value)
            return True
        except ValueError:
            return False

    vcmd_ftth = (dscm_frame.register(validate_ftth), "%P")
    vcmd_contact = (dscm_frame.register(validate_contact), "%P")
    vcmd_amount = (dscm_frame.register(validate_amount), "%P")


    #######################################################
    y_pos = 30

    for field in fields:
        lbl = ctk.CTkLabel(
            dscm_frame, text=field,
            font=("Arial", 15),
            text_color="white"
        )
        lbl.place(x=20, y=y_pos)

        ############################ Entry Creation Loop
        if field == "FTTH No":
            widget = ctk.CTkEntry(
                dscm_frame,
                width=200,
                fg_color="white",
                text_color="black",
                validate="key",
                validatecommand=vcmd_ftth
            )

        elif field == "Contact No":
            widget = ctk.CTkEntry(
                dscm_frame,
                width=200,
                fg_color="white",
                text_color="black",
                validate="key",
                validatecommand=vcmd_contact
            )

        elif field == "Bill Amount":
            widget = ctk.CTkEntry(
                dscm_frame,
                width=200,
                fg_color="white",
                text_color="black",
                validate="key",
                validatecommand=vcmd_amount
            )

        elif field == "Cash Received":
            widget = ctk.CTkEntry(
                dscm_frame,
                width=200,
                fg_color="white",
                text_color="black",
                validate="key",
                validatecommand=vcmd_amount
            )

        elif field == "Balance":
            widget = ctk.CTkEntry(
                dscm_frame,
                width=200,
                fg_color="lightgrey",
                text_color="black",
                state="disabled"  # 🔒 Prevent manual editing
            )


        elif field == "Cash With":
            widget = ctk.CTkComboBox(
                dscm_frame,
                width=200,
                values=["COUNTER", "IOB-ACCOUNT", "TEKNIX", "BETA-ACCOUNT", "CUSTOMER", "OTHERS"],
                fg_color="white",
                text_color="black"
            )
            widget.set("COUNTER")

        else:
            widget = ctk.CTkEntry(
                dscm_frame,
                width=200,
                fg_color="white",
                text_color="black"
            )

        widget.place(x=180, y=y_pos)
        entries[field] = widget
        y_pos += 50

    # ---------- AUTO BALANCE CALCULATION ----------
    def calculate_balance(event=None):
        bill = entries["Bill Amount"].get().strip()
        cash = entries["Cash Received"].get().strip()

        try:
            bill_value = float(bill) if bill else 0
            cash_value = float(cash) if cash else 0
            balance = bill_value - cash_value
        except ValueError:
            balance = 0

        entries["Balance"].configure(state="normal")
        entries["Balance"].delete(0, "end")
        entries["Balance"].insert(0, f"{balance:.2f}")

        # 🔴 Turn red if negative
        if balance < 0:
            entries["Balance"].configure(text_color="red")
        else:
            entries["Balance"].configure(text_color="black")

        entries["Balance"].configure(state="disabled")

    # ---------- VALIDATION FUNCTION ----------
    def validate_entries():
        for field, widget in entries.items():
            value = widget.get().strip()

            if field in ["FTTH No", "Contact No"]:
                if len(value) != 10:
                    check_btn.configure(state="disabled")
                    return

            elif field != "Cash With" and value == "":
                check_btn.configure(state="disabled")
                return

        check_btn.configure(state="normal")

    # ---------- CHECK BUTTON ACTION ----------

    def show_verification():
        popup = ctk.CTkToplevel(parent)
        popup.title("Verification")
        popup.geometry("450x500")
        popup.transient(parent)
        popup.grab_set()  # 🔒 MODAL
        popup.resizable(False, False)

        popup_frame = ctk.CTkFrame(popup)
        popup_frame.pack(fill="both", expand=True, padx=10, pady=10)

        popup_frame.columnconfigure(0, weight=1)
        popup_frame.columnconfigure(1, weight=2)

        title = ctk.CTkLabel(
            popup_frame,
            text="Verification Details",
            font=("Arial", 18, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        row = 1
        for field, widget in entries.items():
            value = widget.get()

            ctk.CTkLabel(
                popup_frame,
                text=field,
                anchor="w"
            ).grid(row=row, column=0, padx=10, pady=6, sticky="w")

            ctk.CTkLabel(
                popup_frame,
                text=value,
                anchor="w"
            ).grid(row=row, column=1, padx=10, pady=6, sticky="w")

            row += 1

        # Buttons
        btn_frame = ctk.CTkFrame(popup_frame)
        btn_frame.grid(row=row, column=0, columnspan=2, pady=20)

        ctk.CTkButton(
            btn_frame,
            text="Back",
            width=100,
            command=popup.destroy
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            btn_frame,
            text="Confirm",
            width=100,
            fg_color="green",
            command=lambda: [print("Confirmed"), popup.destroy()]
        ).pack(side="left", padx=10)

    # ---------- Buttons ----------
    check_btn = ctk.CTkButton(
        dscm_frame,
        text="Check",
        width=100,
        fg_color="green",
        text_color="white",
        state="disabled",  # 🔒 initially disabled
        command=show_verification
    )
    check_btn.place(x=60, y=y_pos + 20)
    for field, widget in entries.items():
        if field != "Cash With":
            widget.bind("<KeyRelease>", lambda event: validate_entries())

    # Bind auto calculation
    entries["Bill Amount"].bind("<KeyRelease>", calculate_balance)
    entries["Cash Received"].bind("<KeyRelease>", calculate_balance)

    # ---------- ENTER KEY NAVIGATION ----------
    entries["Bill Amount"].bind("<Return>",
        lambda event: entries["Cash Received"].focus())

    entries["Cash Received"].bind("<Return>",
        lambda event: entries["Balance"].focus())

    ####################

    def clear_entries():
        for widget in entries.values():
            if hasattr(widget, "delete"):
                widget.delete(0, "end")

        validate_entries()  # 🔄 re-check after clearing

    cancel_btn = ctk.CTkButton(
        dscm_frame,
        text="Cancel",
        width=100,
        fg_color="red",
        text_color="white",
        command=clear_entries  # clears instead of destroying
    )
    cancel_btn.place(x=200, y=y_pos + 20)

    ####################

    return dscm_frame

