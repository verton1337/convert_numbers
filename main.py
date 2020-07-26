from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout 
def rymskie(max_number):
    otvet = ""
    dicton = {"1":"I","2":"II","3":"III","4":"IV","5":"V","6":"VI","7":"VII","8":"VIII","9":"IX","10":"X","40":"XL","50":"L","90":"XC","100":"C","500":"D","1000":"M"}
    if str(max_number) in dicton:
        otvet = dicton[str(max_number)]
    elif max_number>10 and max_number<40:
        for i in range(int(str(max_number)[0])):
            otvet += dicton["10"]
        otvet += dicton[str(max_number)[1]]
    elif max_number>40 and max_number<50:
        otvet+=dicton["40"]
        otvet += dicton[str(max_number)[1]]
    elif max_number>50 and max_number<90:
        otvet+=dicton["50"]
        otvet += rymskie(max_number-50)
    elif max_number>90 and max_number<100:
        otvet+=dicton["90"]
        otvet += dicton[str(max_number)[1]]
    elif max_number>100 and max_number<500:
        a = max_number//100
        otvet += dicton["100"]* a
        otvet += rymskie(max_number-a*100)
    elif max_number>500 and max_number<1000:
        otvet += dicton["500"]
        otvet += rymskie(max_number-500)
    elif  max_number>1000:
        a = max_number//1000
        otvet += dicton["1000"]* a
        otvet += rymskie(max_number-a*1000)
    return otvet
def arabskie(max_number):
    result = 0
    # problem to 4, 9, 40 and 90
    dicton = {"I":"1","V":"5","X":"10","L":"50","C":"100","D":"500","M":"1000"}
    for i in max_number:
        if  i not in dicton.keys():
            return " Вводите римские цифры!\n (Пример - MDXII)"    
    for i in range(len(max_number)):
        try:
            if max_number[i] == "I" and (max_number[i+1] == "V" or max_number[i+1] == "X"):
                result-=2
            if max_number[i] == "X" and (max_number[i+1] == "L" or max_number[i+1] == "C"):
                result-=20
        except IndexError:
            continue
    for i in max_number:
            result+=int(dicton[i])
    return result 

class GameApp(App):
	def operationArab(self, instance):
		try:
			self.lbl.text = str(arabskie(self.lbl.text))
		except: self.lbl.text += "- такое число не возможно конвертировать в Арабские" 
	def operationRym(self,instance):
		try:
			self.lbl.text = rymskie(int(self.lbl.text))
		except: self.lbl.text += "- такое число не возможно конвертировать в Римские" 
	def build(self):
		bl = BoxLayout(orientation = "vertical", spacing = 3)
		bl2 = BoxLayout(size_hint = (1, .4), padding = [0,100,0,0])
		self.lbl = TextInput(text = "Введите число", size_hint=(1, .2))
		bl.add_widget(self.lbl)
		bl2.add_widget(Button(text = "В Римские", on_press = self.operationRym))
		bl2.add_widget(Button(text = "В Арабские", on_press = self.operationArab))
		bl.add_widget(bl2)
	

		return bl

if __name__ == "__main__":
	GameApp().run()