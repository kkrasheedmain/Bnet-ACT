import customtkinter as ctk
from datetime import datetime

def create_cbp_frame(parent):
    cbp_frame = ctk.CTkFrame(parent, fg_color="grey")
    cbp_frame.place(relwidth=1, relheight=1)

    fields = [
        "Date",
        "Customer Name",
        "Mobile No",
        "Amount",
        "Payment Mode",
        "Remarks"
    ]

    entries = {}

    y_pos = 30

    for field in fields:
        lbl = ctk.CTkLabel(
            cbp_frame,
            text=field,
            font=("Arial", 15),
            text_color="white"
        )
        lbl.place(x=20, y=y_pos)

        # ---------- FIELD TYPES ----------
        if field == "Date":
            widget = ctk.CTkEntry(cbp_frame, width=240, fg_color="lightgrey")
            widget.insert(0, datetime.now().strftime("%Y-%m-%d"))
            widget.configure(state="readonly")

        elif field == "Mobile No":
            widget = ctk.CTkEntry(cbp_frame, width=240)

            # simple validation
            def validate_mobile(new_value):
                return new_value.isdigit() and len(new_value) <= 10 or new_value == ""

            vcmd = (cbp_frame.register(validate_mobile), "%P")
            widget.configure(validate="key", validatecommand=vcmd)

        elif field == "Payment Mode":
            widget = ctk.CTkComboBox(
                cbp_frame,
                width=240,
                values=["CASH", "UPI", "BANK", "CARD"]
            )
            widget.set("CASH")

        else:
            widget = ctk.CTkEntry(cbp_frame, width=240)

        widget.place(x=220, y=y_pos)
        entries[field] = widget
        y_pos += 50

    # ---------- VALIDATION ----------
    def validate_entries():
        if entries["Customer Name"].get().strip() == "":
            check_btn.configure(state="disabled")
            return
        if len(entries["Mobile No"].get()) != 10:
            check_btn.configure(state="disabled")
            return
        if entries["Amount"].get().strip() == "":
            check_btn.configure(state="disabled")
            return

        check_btn.configure(state="normal")

    for field, widget in entries.items():
        if field not in ["Payment Mode", "Date"]:
            widget.bind("<KeyRelease>", lambda e: validate_entries())

    # ---------- BUTTONS ----------
    def clear_entries():
        for field, widget in entries.items():
            if field == "Date":
                widget.configure(state="normal")
                widget.delete(0, "end")
                widget.insert(0, datetime.now().strftime("%Y-%m-%d"))
                widget.configure(state="readonly")
            elif field == "Payment Mode":
                widget.set("CASH")
            else:
                widget.delete(0, "end")
        check_btn.configure(state="disabled")

    check_btn = ctk.CTkButton(
        cbp_frame,
        text="Check",
        width=100,
        fg_color="green",
        state="disabled"
    )
    check_btn.place(x=60, y=y_pos + 20)

    cancel_btn = ctk.CTkButton(
        cbp_frame,
        text="Cancel",
        width=100,
        fg_color="red",
        command=clear_entries
    )
    cancel_btn.place(x=200, y=y_pos + 20)

    return cbp_frame
