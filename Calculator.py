from tkinter import *

class Application(Frame):#Frame groups n organizes widgets and acts a container
    def __init__(self,master): #master represents parent widget
        super(Application,self).__init__(master) #super is a builtin func which returns a proxy object to make method calls to a class that can be a parent or a sibling in nature.
        self.task = "" #task is a subclass of future.Future is an object that's supposed to have a result in future.
        self.UserIn=StringVar()
        self.grid() #grid registers a widget using geometry manager to make it visible on screen
                    #geometry manager manages the placement of elements of the GUI.
        self.create_widgets()

    def create_widgets(self):
        self.user_input = Entry(self, bg ="#555AAC", bd = 29, insertwidth = 4, width= 24,
        font=("Verdana",20, "bold"), textvariable= self.UserIn, justify= RIGHT)
        self.user_input.grid(columnspan = 4)
        
        self.user_input.insert(0,"0")#sets initial value of calculator to 0
                        #Entry accepts single line text strings from user. txt widget accepts multiline texts that can be edited.
                        #label accepts multiline strings that can't be edited.
                        #bg is bckgrnd color,bd is bolder,insertwidth is width of insertion cursor,
                        #its height is determined by the tallest item in its line.default is 2px.Width is width of widget and measured in characters,not pixel.

        self.button1=Button(self, bg="white", bd=12, text="7", padx= 33, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick(7))
        self.button1.grid(row=2, column=0, sticky=W) #sticky distributes extra spaces not utilised by the widget.W value stretches the widget both horizontally n vertically to use the spaces.
        #row implies the row no. to insert the widget.counting starts from 0.


        self.button2=Button(self, bg="white", bd=12, text="8", padx= 33, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick(8))
        self.button2.grid(row=2, column=1, sticky=W)

        self.button3=Button(self, bg="white", bd=12, text="9", padx= 33, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick(9))
        self.button3.grid(row=2, column=2, sticky=W)

        self.button4=Button(self, bg="white", bd=12, text="4", padx= 33, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)

        self.button5=Button(self, bg="white", bd=12, text="5", padx= 33, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick(5))
        self.button5.grid(row=3, column=1, sticky=W)

        self.button6=Button(self, bg="white", bd=12, text="6", padx= 33, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)

        self.button7=Button(self, bg="white", bd=12, text="1", padx= 33, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick(1))
        self.button7.grid(row=4, column=0, sticky=W)

        self.button8=Button(self, bg="white", bd=12, text="2", padx= 33, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick(2))
        self.button8.grid(row=4, column=1, sticky=W)

        self.button9=Button(self, bg="white", bd=12, text="3", padx= 33, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick(3))
        self.button9.grid(row=4, column=2, sticky=W)

        self.button0=Button(self, bg="Gold", bd=12, text="0", padx= 33, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick(0))
        self.button0.grid(row=5, column=0, sticky=W)

        self.Addbutton=Button(self, bg="white", bd=12, text="+", padx= 35, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick("+"))
        self.Addbutton.grid(row=2, column=3, sticky=W)

        self.Subbutton=Button(self, bg="white", bd=12, text="-", padx= 39, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick("-"))
        self.Subbutton.grid(row=3, column=3, sticky=W)

        self.Mulbutton=Button(self, bg="white", bd=12, text="*", padx= 38, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick("*"))
        self.Mulbutton.grid(row=4, column=3, sticky=W)

        self.Divbutton=Button(self, bg="white", bd=12, text="/", padx= 39, pady=25,
        font=("Helvetica",20,"bold"),command = lambda : self.buttonClick("/"))
        self.Divbutton.grid(row=5, column=3, sticky=W)

        self.Equalbutton=Button(self, bg="#80ff00", bd=12, text="=", padx= 100, pady=25,
        font=("Helvetica",20,"bold"),command = self.CalculateTask)
        self.Equalbutton.grid(row=5, column=1, sticky=W, columnspan = 2 )

        self.Clearbutton=Button(self, bg="Red", bd=12, text="AC", padx= 84, pady=25,
        font=("Helvetica",20,"bold"),command = self.ClearDisplay)
        self.Clearbutton.grid(row=1, sticky=W, columnspan = 4 )

    def buttonClick(self,number):
        self.task= str(self.task)+ str(number) #makes string addition on calculator screen.like pressing 5 two times becomes 55.
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data=self.user_input.get()
        try:
            self.answer= eval(self.data) #evaluates expression.for eg  eval(1+1) =2
            self.displayText(self.answer)
            self.task=self.answer #the input screen now displays the answer of the expression.
        except SyntaxError as e:
            self.displayText("Invalid Syntax!")
            self.task= ""

    def displayText(self,value):
        self.user_input.delete(0,END)
        self.user_input.insert(0,value)

    def ClearDisplay(self):
        self.task=""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")                     

calculator  = Tk()

calculator.title("Calculator")
app=Application(calculator)

calculator.resizable(width= False, height= False) #makes the calculator window non resizable

calculator.mainloop() 

        
                            
