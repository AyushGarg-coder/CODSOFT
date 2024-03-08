import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

Builder.load_file("calculator.kv")

class calculator(Widget):
    def number(self,values):
        result=self.ids.text_number.text
        if '0' in result[0] and '.' not in result:
            result=""
            self.ids.text_number.text=f'{result}{str(values)}'
        else:
            self.ids.text_number.text=f'{result}{str(values)}'
        
    def maths(self,sign):
        result=self.ids.text_number.text
        self.ids.text_number.text=f'{result}{sign}'

    def clear(self):
        self.ids.text_number.text="0"
    
    def remove(self):
        result=self.ids.text_number.text
        self.ids.text_number.text=f'{result[:-1]}'

    def minus_plus(self):
        result=self.ids.text_number.text
        if "-" in result:
            self.ids.text_number.text=f'{result.replace("-","")}'
        else:
            self.ids.text_number.text=f'-{result}'

    def dot(self):
        result=self.ids.text_number.text
        number_plus=result.split("+")
        number_minus=result.split("-")
        number_div=result.split("/")
        number_mul=result.split("*")
        number_mod=result.split("%")
        if ("+" or "-" or "-" or "/" or "%") in result and ("." not in number_plus[-1] or "." not in number_minus[-1] or '.' not in number_div[-1] or "." not in number_mul[-1] or "." not in number_mod[-1]):
            self.ids.text_number.text=f'{result}.'
        elif "." in result:
            pass
        else:
            self.ids.text_number.text=f'{result}.'

    def evaluate(self):
        result=self.ids.text_number.text
        self.ids.text_number.text=f'{eval(result)}'

class CALCULATOR(App):
    def build(self):
        
        return calculator()
    
if __name__=='__main__':
    CALCULATOR().run()
