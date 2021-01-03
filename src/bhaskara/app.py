"""
App que calcula a formula de Bhaskara
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import math

class Bhaskara(toga.App):
    def startup(self):
        # CRIAR COMPONENTES
        form = toga.Box(style=Pack(direction=COLUMN, padding=5))

        self.divider = toga.Label(' ', style=Pack(padding=(0, 5)))

        self.lbl_A = toga.Label('A: ', style=Pack(padding=(0, 5)))
        self.input_A = toga.NumberInput(style=Pack(flex=1))

        self.lbl_B = toga.Label('B: ', style=Pack(padding=(0, 5)))
        self.input_B = toga.NumberInput(style=Pack(flex=1))

        self.lbl_C = toga.Label('C: ', style=Pack(padding=(0, 5)))
        self.input_C = toga.NumberInput(style=Pack(flex=1))

        self.lbl_X1 = toga.Label('X¹: ', style=Pack(padding=(0, 5)))
        self.input_X1 = toga.TextInput(style=Pack(flex=1), on_change=False, readonly=True)

        self.lbl_X2 = toga.Label('X²: ', style=Pack(padding=(0, 5)))
        self.input_X2 = toga.TextInput(style=Pack(flex=1), on_change=False, readonly=True)

        self.btnCalcular = toga.Button('Calcular', on_press=self.calcular, style=Pack(padding=(0,5)))

        # ADICIONA NO FORM
        form.add(self.lbl_A)
        form.add(self.input_A)
        form.add(self.lbl_B)
        form.add(self.input_B)
        form.add(self.lbl_C)
        form.add(self.input_C)

        form.add(self.divider)
        form.add(self.btnCalcular)
        form.add(self.divider)
        
        form.add(self.lbl_X1)
        form.add(self.input_X1)
        form.add(self.lbl_X2)
        form.add(self.input_X2)
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = form
        self.main_window.show()

    def calcular(self, widget):
        a = int(self.input_A.value)
        b = int(self.input_B.value)
        c = int(self.input_C.value)
        
        delta=(b**2)-(4*a*c)
        
        if delta<0 :
            self.main_window.info_dialog('Atenção', "Raiz negativa nao pode ser extraida.")
            self.limpar_campos()
        else :
            x=math.sqrt(delta)
            x1=(-b+x)/(2*a)
            x2=(-b-x)/(2*a)

            self.input_X1.value = x1
            self.input_X2.value = x2

    def limpar_campos(self):
        self.input_A.value = 0
        self.input_B.value = 0
        self.input_C.value = 0

        self.input_X1.clear()
        self.input_X2.clear()

def main():
    return Bhaskara()