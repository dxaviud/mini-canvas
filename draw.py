from tkinter import Tk, Canvas
from PIL import ImageGrab

class Drawing():

    def __init__(self):
        self.__save_count = 1

    def display(self):

        root = Tk()

        canvas = Canvas(root, width=500, height=500)
        canvas.grid(row=0, column=0)

        brush_shape = "square"
        brush_thickness = 5
        draw_color = "black"

        def draw(event):
            if brush_shape == "square":
                canvas.create_rectangle(event.x-brush_thickness, event.y-brush_thickness, event.x+brush_thickness, event.y+brush_thickness, fill=draw_color, outline=draw_color)
            elif brush_shape == "oval":
                canvas.create_oval(event.x-brush_thickness, event.y-brush_thickness, event.x+brush_thickness, event.y+brush_thickness, fill=draw_color, outline=draw_color)
        
        canvas.bind("<B1-Motion>", draw)
        canvas.bind("<ButtonPress>", draw)

        def save_as_png(widget):
            x = root.winfo_rootx() + widget.winfo_x()
            y = root.winfo_rooty() + widget.winfo_y()
            x1 = x + widget.winfo_width()
            y1 = y + widget.winfo_height()
            ImageGrab.grab().crop((x,y,x1,y1)).save("my-canvas-" + str(self.__save_count) + ".png")
            self.__save_count += 1

        def key_press(event):
            nonlocal draw_color
            nonlocal brush_shape
            nonlocal brush_thickness

            key = event.char.upper()

            try:
                new_brush_thickness = int(key)
                brush_thickness = new_brush_thickness
            except:
                if key == "C":
                    canvas.delete("all")
                elif key == "R":
                    draw_color = "red"
                elif key == "G":
                    draw_color = "green"
                elif key == "B":
                    draw_color = "blue"
                elif key == "Y":
                    draw_color = "yellow"
                elif key == "S":
                    brush_shape = "square"
                elif key == "O":
                    brush_shape = "oval"
                elif key == "=":
                    save_as_png(canvas)
                else:
                    draw_color = "black"

        canvas.bind("<KeyPress>", key_press)
        canvas.focus_set()

        root.mainloop()

if __name__ == "__main__":
    app = Drawing()
    app.display()