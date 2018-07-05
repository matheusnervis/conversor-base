from tkinter import *
from tkinter import font
from tkinter import messagebox

BIN_OCT = dict([('%03d' % int(bin(i)[2:]), hex(i)[2:]) for i in range(8)])
BIN_HEX = dict([('%04d' % int(bin(i)[2:]), hex(i)[2:]) for i in range(16)])
OCT_BIN = dict([(hex(i)[2:], '%03d' % int(bin(i)[2:])) for i in range(8)])
HEX_BIN = dict([(hex(i)[2:], '%04d' % int(bin(i)[2:])) for i in range(16)])

class App:

    def __init__(self, win):

        self.win = win
        self.font = font.Font(window, ('Helvetica', 16))

        self.win.title('Conversor de Bases')
        self.win.geometry('350x300+200+200')
        self.win.resizable(width=False, height=False)
        
        self.op = IntVar()
        self.op.set(8)
        
        self.frame = Frame(self.win, width=350, height=0)
        self.frame.grid(column=0, row=0)
        self.frame.grid_propagate(0)
        
        self.lbframe_op = LabelFrame(self.win, width=240, text='Opções de conversão')
        self.lbframe_op.grid(column=0, row=0, padx=5, pady=5, sticky=E+W)
        self.lbframe_op['font']=self.font
        self.radio_btn_oct = Radiobutton(self.lbframe_op, text='oct -> hex', variable=self.op, value=8)
        self.radio_btn_oct.grid(column=0, row=0)
        self.radio_btn_oct['font']=self.font
        self.radio_btn_hex = Radiobutton(self.lbframe_op, text='hex -> oct', variable=self.op, value=16)
        self.radio_btn_hex.grid(column=0, row=1)
        self.radio_btn_hex['font'] = self.font
        
        self.num = Entry(self.win)
        self.num.grid(column=0, row=1, padx=5, pady=5, sticky=E+W)
        self.num['font'] = self.font
        
        self.btn_conv = Button(self.win, text='Converter', command = self.convert)
        self.btn_conv.grid(column=0, row=2)
        self.btn_conv['font'] = self.font
        
        self.lb_result = Label(self.win, bg='#ffffff', relief=SUNKEN)
        self.lb_result.grid(column=0, row=3, padx=5, pady=5, sticky=E+W)
        self.lb_result['font'] = self.font

    def convert(self):

        _ = (OCT_BIN, BIN_HEX) if self.op.get() == 8 else (HEX_BIN, BIN_OCT)
        x = 4 if self.op.get() == 8 else 3

        try:
            num = ''.join(_[0][i] for i in self.num.get().lower())
        except KeyError:
            messagebox.showwarning('Entrada inválida','Entrada inválida')
            return

        num = '0'*(x - (len(num)%x)) + num
        print(num)
        num_conv = ''

        for i in range(len(num) // x):
            num_conv += _[1][num[0+(i*x) : x+(i*x)]]

        if num_conv != '0' and num_conv[0] == '0':
            num_conv = num_conv[1:]

        self.lb_result['text'] = num_conv.upper()

    # def convert(self):
    #     try:
    #         base = self.op.get()
    #         num = int(self.num.get(), base=base)
    #         self.lb_result['text'] = oct(num)[2:] if base == 16 else hex(num)[2:]
    #     except KeyError:
    #         messagebox.showwarning('Entrada inválida','Entrada inválida')
    #         return


window = Tk()
window.wm_iconbitmap('conv.ico')
app = App(window)
window.mainloop()
