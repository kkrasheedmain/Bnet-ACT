import customtkinter as ctk
from support_functions import create_side_frame,create_dscm_frame

if __name__ == '__main__':

    window = ctk.CTk()
    window.configure(fg_color="#1e90ff")
    window.title("One-Solution")
    window.geometry("800x600")
    window.iconbitmap("icon-Bharat BNET.ico")
    window.resizable(False, False)

    # import sidebar
    side_frame = create_side_frame(window)
    side_frame.pack(side='left', fill='y', padx=5, pady=5)

    #main_frame
    main_frame= create_dscm_frame(window)
    main_frame.pack(side='left', fill='both', expand=True, pady=5, padx=5)



    window.mainloop()
