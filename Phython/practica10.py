import tkinter as tk
from tkinter import messagebox

def insertion_sort_with_counts(arr):
    steps = []
    array = arr[:]
    comparisons = 0
    movements = 0

    steps.append(array[:])

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            comparisons += 1
            array[j + 1] = array[j]
            movements += 1
            j -= 1

        if j >= 0:
            comparisons += 1

        array[j + 1] = key
        movements += 1

        steps.append(array[:])

    return steps, comparisons, movements

def on_sort():
    input_data = entry.get()
    try:
        arr = [int(x.strip()) for x in input_data.split(",") if x.strip() != ""]
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números separados por comas.")
        return

    steps, comparisons, movements = insertion_sort_with_counts(arr)

    steps_text.delete(1.0, tk.END)
    for idx, step in enumerate(steps):
        highlighted = ' '.join(
            [f"[{num}]" if i <= idx else str(num) for i, num in enumerate(step)]
        )
        steps_text.insert(tk.END, f"Iteración {idx}: {highlighted}\n")

    comp_label.config(text=f"Comparaciones: {comparisons}")
    move_label.config(text=f"Movimientos: {movements}")

# GUI
root = tk.Tk()
root.title("Algoritmo de Inserción - Python GUI")
root.geometry("700x500")
root.configure(bg="white")

frame = tk.Frame(root, bg="white")
frame.pack(padx=20, pady=20, fill="both", expand=True)

title = tk.Label(frame, text="Ejemplo Práctico: Inserción", font=("Arial", 16, "bold"), fg="#d96a00", bg="white")
title.pack(pady=(0, 10))

entry_label = tk.Label(frame, text="Ingresa números separados por comas:", font=("Arial", 12), bg="white")
entry_label.pack(anchor="w")

entry = tk.Entry(frame, width=60, font=("Arial", 12))
entry.insert(0, "8,7,5,9,1,6,2,4,3")
entry.pack(pady=5)

sort_button = tk.Button(frame, text="Ordenar con Inserción", bg="#d96a00", fg="white", font=("Arial", 12, "bold"), command=on_sort)
sort_button.pack(pady=10)

steps_label = tk.Label(frame, text="Pasos del algoritmo:", font=("Arial", 12, "bold"), fg="#c75a00", bg="white")
steps_label.pack(anchor="w", pady=(10, 5))

steps_text = tk.Text(frame, height=10, font=("Courier", 10), bg="#f9f9f9", wrap="word")
steps_text.pack(fill="both", expand=True)

counters_frame = tk.Frame(frame, bg="white")
counters_frame.pack(pady=10)

comp_label = tk.Label(counters_frame, text="Comparaciones: 0", font=("Arial", 12), bg="white")
comp_label.pack(side="left", padx=10)

move_label = tk.Label(counters_frame, text="Movimientos: 0", font=("Arial", 12), bg="white")
move_label.pack(side="left", padx=10)

# Carga inicial
on_sort()

root.mainloop()
