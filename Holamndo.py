import tkinter as tk
from tkinter import ttk, Canvas, filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class CADSoftware:
    def __init__(self, root):
        self.root = root
        self.root.title("Software CAD para Paredes de Casas")

        self.create_widgets()

    def create_widgets(self):
        # Frame para los controles
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label y Entry para la altura del muro
        ttk.Label(control_frame, text="Altura del Muro:").grid(row=0, column=0, sticky=tk.W)
        self.height_var = tk.StringVar()
        self.height_entry = ttk.Entry(control_frame, textvariable=self.height_var)
        self.height_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        # Label y Combobox para el tipo de madera
        ttk.Label(control_frame, text="Tipo de Madera:").grid(row=1, column=0, sticky=tk.W)
        self.wood_type_var = tk.StringVar()
        self.wood_type_combobox = ttk.Combobox(control_frame, textvariable=self.wood_type_var)
        self.wood_type_combobox['values'] = ('2x4', '2x6', '2x8')
        self.wood_type_combobox.grid(row=1, column=1, sticky=(tk.W, tk.E))

        # Botón para dibujar el muro
        self.draw_button = ttk.Button(control_frame, text="Dibujar Muro", command=self.draw_wall)
        self.draw_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Canvas para el dibujo
        self.canvas_frame = ttk.Frame(self.root, padding="10")
        self.canvas_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.canvas = Canvas(self.canvas_frame, width=800, height=600, bg="white")
        self.canvas.pack()

    def draw_wall(self):
        try:
            height = float(self.height_var.get())
        except ValueError:
            print("Por favor, introduce una altura válida.")
            return

        wood_type = self.wood_type_var.get()
        if wood_type not in ('2x4', '2x6', '2x8'):
            print("Por favor, selecciona un tipo de madera válido.")
            return

        # Dibujar un rectángulo simple como representación del muro
        self.canvas.create_rectangle(50, 50, 50 + 100, 50 + height, fill="lightgrey", outline="black")
        self.canvas.create_text(100, 50 + height / 2, text=f"{wood_type}", anchor=tk.W)

if __name__ == "__main__":
    root = tk.Tk()
    app = CADSoftware(root)
    root.mainloop()
