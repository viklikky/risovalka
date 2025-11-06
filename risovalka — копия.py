import tkinter
import tkinter.ttk
import os

class App:

    def __init__(self, name):
        self.name = name
        self.cursor_x = 0
        self.cursor_y = 0
        self.current_width = 40
        self.current_color = 'crimson'
        self.number = 0



    def create_palette(self):
        self.palette = tkinter.PhotoImage(file='bin/color_section.png')
        self.palette_box = tkinter.Label(
                master=self.window,
                image=self.palette,
                bg='#777',
            )
        self.palette_box.place(x=10, y=20)


    def change_current_color(self, event):
        #print(event.widget['bg'])
        self.current_color = event.widget['bg']
    

    def  create_color_boxes(self):

        

        for offset in range(7):
            color = '#' + os.urandom(3).hex()
            color_box = tkinter.Label(master=self.window, bg=color, width=4, height=2)

            color_box.place(x=33 + self.number, y=55 + offset * 55)
            color_box.bind('<Button-1>', self.change_current_color )

        #self.number += 10
        
    
    def randomize_color_boxes(self):
            self.create_color_boxes()


    def create_new_color_boxes_button(self):


            
        self.random_button_image = tkinter.PhotoImage(file='bin\\eraser.png')
        self.random_color_button = tkinter.Button(
            master=self.window,
            image=self.random_button_image,
            bd='0',
            command=self.randomize_color_boxes
            #text='kkk'

        )

        self.random_color_button.place(x=33, y=440)




    def set_current_cursor_xy(self, event):
        self.cursor_x = event.x
        self.cursor_y = event.y 
       
        

    def create_canvas(self):
        self.canvas = tkinter.Canvas(
            master=self.window,
            width=930,
            height=500,
            bg='white',
            cursor='tcross'
        )
        self.canvas.bind('<Button-1>', self.set_current_cursor_xy)
        self.canvas.bind('<B1-Motion>', self.make_art)

        self.canvas.place(x=100, y=10)


    def change_current_width(self, event):
        self.current_width = event
        self.current_width_text['text'] = round(float(event), 1)
        print(type(event))


    def create_width_slider_text(self):
        self.current_width_text = tkinter.Label(
            master=self.window,
            text='0',
            bg='#777',
            fg='#fff',
            font=('arial', 20)

        )

        self.current_width_text.place(x=250, y=524)


##    def slider_changed(value):
##        #print(value, current_slider_value.get())
##        slider_value['text'] = f'{current_slider_value.get():.2f}'
##
##

    def create_width_slider(self):
        self.slider = tkinter.ttk.Scale(
            master=self.window,
            from_=1, to=100,
            command=self.change_current_width
        )

        self.slider.place(x=100, y=530)

    def make_art(self, event):
        #color = '#' + os.urandom(3).hex()
       
        self.canvas.create_line(
            [self.cursor_x, self.cursor_y, event.x, event.y],
            width=self.current_width,
            fill=self.current_color,
            capstyle=tkinter.ROUND

        )
        self.cursor_x, self.cursor_y = event.x, event.y
      

    def run(self):
        
        # Main Window

        self.window = tkinter.Tk()
        self.window.title(self.name)
        self.window.geometry('1050x570+270+160')
        self.window.resizable(False, False)
        self.window.config(bg='#777')

        self.logo = tkinter.PhotoImage(file='bin/logo.png')
        self.window.iconphoto(False, self.logo)

        self.create_palette()
        self.create_color_boxes()
        self.create_canvas()
        self.create_width_slider()
        self.create_width_slider_text()
        self.create_new_color_boxes_button()






program = App('Risovalka')
program.run()








##
##
##
### Icon
##
##
### Palette box
##
##
##
##)
##
##
##
### Colors
##
##colors_box = tkinter.Canvas(
##    master=window,
##    width=37,
##    height=300,
##    bg='#ddd'
##)
##
##colors_box.place(x=30, y=60)
##
##
##def display_palette():
##
##    palette = {
##        'crimson': [10, 10, 30, 30],
##        'lime':[10, 40, 30, 60],
##        '#ab2567':[10, 70, 30, 90],
##        'salmon':[10, 100, 30, 120]
##
##    }
##
##    for color_code, color_pos in palette.items():
##        color_box = colors_box.create_rectangle(color_pos, fill=color_code)
##
##        def func(event, color=color_code):
##            change_color(color)
##           
##        
##        colors_box.tag_bind(color_box, '<Button-1>', func)
##
##        #func(None)
##   
##   
##
##    
##display_palette()
##
### Eraser
##
##eraser = tkinter.PhotoImage(file='bin/eraser.png')
##eraser_button = tkinter.Button(
##    master=window,
##    image=eraser,
##    bg='#aaa'
##
##
##)
##eraser_button.place(x=30, y=400)
##
### Add Image
##
##addimage = tkinter.PhotoImage(file='bin/addimage.png')
##addimage_button = tkinter.Button(
##    master=window,
##    image=addimage,
##    bg='#aaa'
##
##
##)
##addimage_button.place(x=30, y=450)
##
##
### Canvas
##

##
##current_x = 0
##current_y = 0
##color = 'cyan'
##
##def locate_xy(event):
##    global current_x,current_y
##    current_x = event.x
##    current_y = event.y
##    
##
##def addline(event):
##    global current_x,current_y
##    canvas.create_line(
##        [current_x, current_y, event.x, event.y ],
##        fill=color,
##        width=current_slider_value.get(),
##        capstyle=tkinter.BUTT,
##        smooth=True
##        )
##    current_x, current_y = event.x, event.y
##        
##canvas.bind('<Button-1>', locate_xy)
##canvas.bind('<B1-Motion>', addline)
##
###canvas.create_rectangle([500, 300, 600, 400], fill='lightpink')
##
### Slider
##
##def slider_changed(value):
##    #print(value, current_slider_value.get())
##    slider_value['text'] = f'{current_slider_value.get():.2f}'
##
##
##current_slider_value = tkinter.DoubleVar()
##
##slider = tkinter.ttk.Scale(
##    master=window,
##    command=slider_changed,
##    from_=0,
##    to=100,
##    variable=current_slider_value
##)
##
##slider.place(x=100, y=530)
##
##slider_value = tkinter.Label(
##    master=window,
##    text='0',
##    bg='#777',
##    fg='#fff',
##    font=('arial', 20)
##)
##
##slider_value.place(x=250, y=524)
##










