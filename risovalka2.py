import tkinter
import tkinter.ttk




# Main Window

window = tkinter.Tk()
window.title('Risovalka')
window.geometry('1050x570+270+160')
window.resizable(False, False)
window.config(bg='#777')



canvas = tkinter.Canvas(
    master=window,
    width=500,
    height=300,
    
)

box1 = canvas.create_rectangle([20, 20, 100, 100], fill='#34ad77')

box2 = canvas.create_rectangle([150, 20, 200, 70], fill='#79e517')



canvas.tag_bind(box2, '<Button-1>', lambda e: print('hi', box2))

canvas.place(x=10, y=10)




print('>>>' * 10)


func = lambda x: print(x)


print(func)


func('labubu')










