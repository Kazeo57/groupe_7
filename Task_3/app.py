import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import threading
import io
from diffusers import StableDiffusionPipeline  # Assurez-vous d'avoir cette importation correcte

def generate_image():
    """
    Cette fonction permet de générer l'image sans l'eregistrer en local en l'envoyant sur l'interface
    """
    spinner.start() 

    # Récupérer le prompt sur l'interface
    prompt = description_entry.get("1.0", tk.END).strip()
    print(f"prompt {prompt}")

    #Génération avec le modèle 
    pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
    generated_image = pipe(prompt).images[0]
    # Convertir l'image générée en format Tkinter
    img_byte_arr = io.BytesIO()
    generated_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    img = Image.open(img_byte_arr)
    img = img.resize((300, 200), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    # Afficher l'image sur l'étiquette d'image
    image_label.config(image=img_tk)
    image_label.image = img_tk

    spinner.stop() 
    
        
def genOnclick():
    """
    Cette fonction qui peret de controller l'interactionentre la génération en parallèle et le running de l'app
    """
    #On vérifie si l'utilisateur a bel et bien entrer un prompt
    if not description_entry.get("1.0",tk.END).strip():
        messagebox.showwarning("Veuiller entrer une description")
    else:
        threading.Thread(target=generate_image).start()

root = tk.Tk()
root.title("Tkinter Application UI")

# Fond d'écran (background)
background_image_path = "background.png"
background_image = Image.open(background_image_path)
image_width, image_height = background_image.size
background_photo = ImageTk.PhotoImage(background_image)
root.geometry(f"{image_width}x{image_height}")

#Incorporation sur le root de l'app
canvas = tk.Canvas(root, width=image_width, height=image_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Position de la zone de description
description_entry = tk.Text(root, height=10, width=35)
description_entry.insert("1.0", "Entrez votre texte ici...")
description_entry.configure(bg="#fef8f3")
description_entry.place(x=74, y=295) 

# Bouton de génération d'image
generate_button = tk.Button(root, text="Générer l'image", command=genOnclick)
generate_button.place(x=420, y=235) 

# Spinner de chargement
spinner = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=100)
spinner.place(x=420, y=270) 

# Zone d'affichage de l'image
image_label = tk.Label(root, bg="#fef8f3")
image_label.place(x=420, y=295, width=300, height=200)  

root.mainloop()
