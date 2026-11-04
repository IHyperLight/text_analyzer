def contar_palabras(texto: str) -> int:
    if not texto.strip():
        return 0
    return len(texto.split())

def contar_caracteres(texto: str) -> int:
    return len(texto)
  
