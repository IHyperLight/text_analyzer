from analyzer.text_analyzer import contar_palabras, contar_caracteres

if __name__ == "__main__":
    texto = "Hola mundo 🦭"
    print(f"Palabras: {contar_palabras(texto)}")
    print(f"Caracteres: {contar_caracteres(texto)}")
  
