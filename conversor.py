from tkinter import *

class App:

    def __init__(self, win):
        self.win = win
        self.op = IntVar()
        self.lbframe_op = LabelFrame(self.win, text='Opções de conversão')
        self.lbframe_op.grid(column=0, row=0)
        self.radio_btn_oct = Radiobutton(self.lbframe_op, text='oct -> hex', variable=self.op, value=8)
        self.radio_btn_oct.grid(column=0, row=0)
        self.radio_btn_hex = Radiobutton(self.lbframe_op, text='hex -> oct', variable=self.op, value=16)
        self.radio_btn_hex.grid(column=0, row=1)
        self.num = Entry(width=15)
        self.num.grid(column=0, row=1)
        self.btn_conv = Button(self.win, text='Converter', command = self.convert)
        self.btn_conv.grid(column=0, row=2)
        self.lb_result = Label(self.win, width=15)
        self.lb_result.grid(column=0, row=3)

    def convert(self):
        pass


window = Tk()
app = App(window)
window.mainloop()