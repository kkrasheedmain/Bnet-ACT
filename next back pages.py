import tkinter as tk


def mov_next_page():
    global count

    if not count > len(pages) - 2:

        count += 1
        for p in pages:
            p.pack_forget()

        page = pages[count]
        page.pack(pady=100)

def mov_back_page():
    global count
    if not count == 0 :
        count-=1
        for p in pages:
            p.pack_forget()

        page=pages[count]
        page.pack(pady=100)


if __name__ == '__main__' :

    window=tk.Tk()
    window.title("One-Solution")
    window.geometry("300x400")
    # icon_file_path=r"D:\Python Projects\Bnet-ACT\icon-Bharat BNET.ico"
    #icon_file_path = "icon-Bharat BNET.ico"
    #window.iconbitmap(icon_file_path)
    #window.resizable(False, False)

    main_frame=tk.Frame(window,bg='white')


    page_1=tk.Frame(main_frame)
    label_pg1=tk.Label(page_1,text="Start Page",font=('Bold',20))
    label_pg1.pack()
    page_1.pack(pady=100)

    page_2 = tk.Frame(main_frame)
    label_pg2 = tk.Label(page_2, text="Second Page", font=('Bold', 20))
    label_pg2.pack()
    #page_2.pack(pady=100)

    page_3 = tk.Frame(main_frame)
    label_pg3 = tk.Label(page_3, text="Third Page", font=('Bold', 20))
    label_pg3.pack()
    #page_3.pack(pady=100)

    page_4 = tk.Frame(main_frame)
    label_pg4 = tk.Label(page_4, text="Last Page", font=('Bold', 20))
    label_pg4.pack()
    #page_4.pack(pady=100)

    main_frame.pack(fill=tk.BOTH, expand=True)
    pages=[page_1,page_2,page_3,page_4]
    count=0

    # def mov_next_page():
    #     global count
    #
    #     if not count > len(pages)-2:
    #
    #         count+=1
    #         for p in pages:
    #             p.pack_forget()
    #
    #         page=pages[count]
    #         page.pack(pady=100)



    bottom_frame = tk.Frame(window)


    back_btn=tk.Button(bottom_frame,text="Back",font=('Bold',12),bg='#333333',fg='white',width=8,command=mov_back_page)
    back_btn.pack(side=tk.LEFT,padx=10)

    next_btn=tk.Button(bottom_frame,text="Next",font=('Bold',12),bg='#123456',fg='white',width=8,command=mov_next_page)
    next_btn.pack(side=tk.LEFT,padx=10)

    bottom_frame.pack(side=tk.BOTTOM, pady=10)


    window.mainloop()

