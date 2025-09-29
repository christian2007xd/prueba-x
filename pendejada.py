import sys
import pikepdf
from pathlib import Path

def reducir_pdf(archivo_entrada):
    try:
        # Nombre del archivo de salida
        archivo_salida = Path(archivo_entrada).stem + "_reducido.pdf"

        # Abrir y optimizar
        pdf = pikepdf.open(archivo_entrada)
        pdf.save(archivo_salida, optimize=True)

        print(f"✅ PDF reducido guardado como: {archivo_salida}")
    except Exception as e:
        print("❌ Error al procesar el PDF:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Arrastra un PDF sobre este script para reducirlo.")
    else:
        reducir_pdf(sys.argv[1])
