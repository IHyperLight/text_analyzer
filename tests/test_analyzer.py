from analyzer.text_analyzer import contar_palabras, contar_caracteres

def test_contar_palabras():
    assert contar_palabras("hola mundo") == 2
    assert contar_palabras("") == 0

def test_contar_caracteres():
    assert contar_caracteres("hola") == 4
  
