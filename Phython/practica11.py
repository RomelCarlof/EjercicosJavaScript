import os
from deep_translator import GoogleTranslator
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def extraer_texto_pdf(ruta_pdf):
    try:
        lector = PdfReader(ruta_pdf)
        texto_completo = ""
        for pagina in lector.pages:
            texto_completo += pagina.extract_text() + "\n"
        return texto_completo
    except Exception as e:
        raise RuntimeError(f"Error al leer el PDF: {e}")

def traducir_texto(texto, src='en', dest='es'):
    try:
        traduccion = GoogleTranslator(source=src, target=dest).translate(texto)
        return traduccion
    except Exception as e:
        raise RuntimeError(f"Error en la traducción: {e}")

def crear_pdf(texto, ruta_salida):
    try:
        c = canvas.Canvas(ruta_salida, pagesize=letter)
        ancho, alto = letter
        margen = 50
        max_ancho = ancho - 2*margen
        max_alto = alto - 2*margen
        line_height = 14
        y = alto - margen

        lineas = texto.split("\n")
        for linea in lineas:
            while linea:
                max_chars = 90
                parte = linea[:max_chars]
                c.drawString(margen, y, parte)
                y -= line_height
                if y < margen:
                    c.showPage()
                    y = alto - margen
                linea = linea[max_chars:]
        c.save()
    except Exception as e:
        raise RuntimeError(f"Error al crear el PDF de salida: {e}")

def main():
    print("Traducción de PDF de Inglés a Español\n")
    ruta_pdf = input("Ingrese la ruta del archivo PDF en inglés:\n").strip()

    if not os.path.isfile(ruta_pdf):
        print("El archivo no existe. Por favor verifique la ruta e intente de nuevo.")
        return

    print("Extrayendo texto del PDF...")
    try:
        texto_ingles = extraer_texto_pdf(ruta_pdf)
        if not texto_ingles.strip():
            print("El PDF no contiene texto extraíble.")
            return
    except Exception as e:
        print(e)
        return

    print("Traduciendo texto...")
    try:
        texto_espanol = traducir_texto(texto_ingles)
    except Exception as e:
        print(e)
        return

    ruta_salida = "resultado_traducido.pdf"
    print(f"Creando PDF traducido: {ruta_salida}")
    try:
        crear_pdf(texto_espanol, ruta_salida)
    except Exception as e:
        print(e)
        return

    print(f"\n¡Traducción completada! Archivo generado: {ruta_salida}")

if __name__ == "__main__":
    main()
