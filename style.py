from tkinter import ttk

def apply_custom_styles(window):
    style = ttk.Style(window)
    style.theme_use("clam")

    style.configure(
        'TCombobox',
        font=('Arial', 11),
        bordercolor='black',
        background='white',
        height=1,
        width=1
    )

    style.configure(
        "TEntry",
        font=("Arial", 11),
        bordercolor="black"
    )

    style.configure(
        "TButton",
        font=("Arial", 11),
        height=1, 
        width=3, 
        bordercolor="black"
    )

    style.configure("Blue.TButton", background="lightblue")
    style.configure("White.TButton", background="white")
    style.configure("Gray.TButton", background="lightgray") 
    style.configure("Red.TButton", background="tomato")
    style.configure("History.TButton", background="white", width=6)
    style.configure("Copy.TButton", background="white", width=5)
    style.configure('Confirm.TButton', background='lightblue', width=7)
    # ===Scientific buttons===
    style.configure('Scientific.Blue.TButton', background='lightblue', width=11)
    style.configure('Scientific.Blue.Small.TButton', background='lightblue', width=4)
    style.configure('Scientific.White.TButton', background='white', width=4)
    style.configure('Scientific.Gray.TButton', background='lightgray', width=4)
    style.configure('Scientific.Yellow.TButton', background='lightyellow', width=4)
    style.configure('Scientific.Green.TButton', background='lightgreen', width=4)
