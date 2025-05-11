import tkinter as tk;
def on_button_click():

    label.config(text="Button clicked!");
    root = tk.Tk()
    root.title("Simple GUI Apllication");

    label = tk.Label(root, text ="Hello World!");
    label.pack(pady=10);

    button = tk.Button(root, text ="Click Me", command=on_button_click);
    button.pack(pady=5);

    root.mainloop();