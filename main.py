import configparser
from pdf2docx import Converter

# Importar archivo config
config = configparser.ConfigParser()
config.read("config.ini")

# Importar valores
pdf_archivo = config["files"]["pdf_ruta"]
word_archivo = config["files"]["word_ruta"]

def convertir_pdf_a_word(pdf_path, word_path):
    """
    Convierte un archivo PDF a un documento de Word, manteniendo texto e imágenes.
    """
    cv = Converter(pdf_path)
    cv.convert(word_path, start=0, end=None)
    cv.close()
    print(f"Conversión completada: {word_path}")

# Ejecutar conversión
convertir_pdf_a_word(pdf_archivo, word_archivo)