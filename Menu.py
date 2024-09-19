import tkinter as tk
from tkinter import messagebox
import threading
import importlib.util

# Variable de control para detener la ejecución
stop_execution = False

def execute_test():
    global stop_execution

    stop_execution = False

    try:
        # Importar el módulo test.py dinámicamente
        spec = importlib.util.spec_from_file_location("test", "test.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Ejecutar test.py en un hilo separado
        thread = threading.Thread(target=module.main)
        thread.start()

    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo test.py no se encontró.")

def execute_test1():
    global stop_execution

    stop_execution = False

    try:
        # Importar el módulo test1.py dinámicamente
        spec = importlib.util.spec_from_file_location("test1", "test1.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Ejecutar test1.py en un hilo separado
        thread = threading.Thread(target=module.main)
        thread.start()

    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo test1.py no se encontró.")

def execute_test2():
    global stop_execution

    stop_execution = False

    try:
        # Importar el módulo test1.py dinámicamente
        spec = importlib.util.spec_from_file_location("test2", "test2.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Ejecutar test1.py en un hilo separado
        thread = threading.Thread(target=module.main)
        thread.start()

    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo test1.py no se encontró.")
def stop_execution():
    global stop_execution
    stop_execution = True

root = tk.Tk()
root.title("Menú de selección")

# Imagen grande
image_path = "logo.png"  # Ruta de la imagen a utilizar
image = tk.PhotoImage(file=image_path)
label_image = tk.Label(root, image=image)
label_image.pack(pady=10)

# Texto "Inteligencia Artificial"
label_ai = tk.Label(root, text="Inteligencia Artificial", font=("Arial", 16))
label_ai.pack(pady=10)

# Nombres y Carnets
names = {
    "Detector": "de señas"


}

for name, carnet in names.items():
    label_name = tk.Label(root, text=f"{name}  {carnet}", font=("Arial", 12))
    label_name.pack()

# Botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_test = tk.Button(frame_buttons, text="Ejecutar lenguaje de señas -Abecedarios-", command=execute_test)
btn_test.pack(side=tk.LEFT, padx=10)

btn_test1 = tk.Button(frame_buttons, text="Ejecutar lenguaje de señas -Palabras-", command=execute_test1)
btn_test1.pack(side=tk.LEFT, padx=10)

btn_test2 = tk.Button(frame_buttons, text="Ejecutar lenguaje de señas -Dias de Semana-", command=execute_test2)
btn_test2.pack(side=tk.LEFT, padx=10)

btn_stop = tk.Button(frame_buttons, text="Detener ejecución", command=stop_execution)
btn_stop.pack(side=tk.LEFT, padx=10)

root.mainloop()
