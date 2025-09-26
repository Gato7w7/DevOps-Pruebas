from src.calculadora import Calculadora

def test_calculadora_suma_con_historial():
    calc = Calculadora()
    resultado = calc.calcular_suma(5, 3)
    
    assert resultado == 8
    assert len(calc.obtener_historial()) == 1
    assert "5 + 3 = 8" in calc.obtener_historial()[0]

def test_multiple_operaciones():
    calc = Calculadora()
    calc.calcular_suma(2, 3)
    calc.calcular_suma(10, 5)
    
    historial = calc.obtener_historial()
    assert len(historial) == 2
    assert "2 + 3 = 5" in historial[0]
    assert "10 + 5 = 15" in historial[1]