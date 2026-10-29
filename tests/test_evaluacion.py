import pytest
from unittest.mock import patch, MagicMock
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from evaluation.madurez_analitica import (
    evaluar_madurez_gartner,
    evaluar_madurez_deltha,
    calcular_puntuacion_global,
    generar_informe_evaluacion,
    NIVELES_GARTNER,
    NIVELES_DELTHA
)


class TestEvaluacionGartner:
    """Pruebas para el modelo de Gartner"""
    
    def test_evaluar_madurez_gartner_nivel_minimo(self):
        """Verifica que con respuestas mínimas se asigna el nivel 1"""
        respuestas = {
            'datos_disponibles': 1,
            'analisis_basico': 1,
            'toma_decisiones': 1,
            'optimizacion': 1,
            'predictivo': 1
        }
        resultado = evaluar_madurez_gartner(respuestas)
        assert resultado['nivel'] == 1
        assert 'Nivel 1' in resultado['descripcion']
    
    def test_evaluar_madurez_gartner_nivel_maximo(self):
        """Verifica que con respuestas máximas se asigna el nivel 5"""
        respuestas = {
            'datos_disponibles': 5,
            'analisis_basico': 5,
            'toma_decisiones': 5,
            'optimizacion': 5,
            'predictivo': 5
        }
        resultado = evaluar_madurez_gartner(respuestas)
        assert resultado['nivel'] == 5
        assert 'Nivel 5' in resultado['descripcion']
    
    def test_evaluar_madurez_gartner_nivel_intermedio(self):
        """Verifica la evaluación en un nivel intermedio"""
        respuestas = {
            'datos_disponibles': 3,
            'analisis_basico': 3,
            'toma_decisiones': 3,
            'optimizacion': 2,
            'predictivo': 2
        }
        resultado = evaluar_madurez_gartner(respuestas)
        assert resultado['nivel'] in [2, 3, 4]
        assert 'puntuacion' in resultado
    
    def test_evaluar_madurez_gartner_respuestas_invalidas(self):
        """Verifica el manejo de respuestas fuera de rango"""
        respuestas_invalidas = {
            'datos_disponibles': 0,
            'analisis_basico': 6,
            'toma_decisiones': 3,
            'optimizacion': 3,
            'predictivo': 3
        }
        with pytest.raises(ValueError):
            evaluar_madurez_gartner(respuestas_invalidas)
    
    def test_evaluar_madurez_gartner_falta_campo(self):
        """Verifica el manejo de campos faltantes"""
        respuestas_incompletas = {
            'datos_disponibles': 3,
            'analisis_basico': 3
        }
        with pytest.raises(KeyError):
            evaluar_madurez_gartner(respuestas_incompletas)


class TestEvaluacionDeltha:
    """Pruebas para el modelo Deltha"""
    
    def test_evaluar_madurez_deltha_nivel_minimo(self):
        """Verifica el nivel inicial en el modelo Deltha"""
        respuestas = {
            'estrategia': 1,
            'gobierno': 1,
            'tecnologia': 1,
            'procesos': 1,
            'personas': 1,
            'cultura': 1
        }
        resultado = evaluar_madurez_deltha(respuestas)
        assert resultado['nivel'] == 1
        assert 'descripcion' in resultado
    
    def test_evaluar_madurez_deltha_nivel_maximo(self):
        """Verifica el nivel avanzado en el modelo Deltha"""
        respuestas = {
            'estrategia': 5,
            'gobierno': 5,
            'tecnologia': 5,
            'procesos': 5,
            'personas': 5,
            'cultura': 5
        }
        resultado = evaluar_madurez_deltha(respuestas)
        assert resultado['nivel'] == 5
    
    def test_evaluar_madurez_deltha_calculo_por_dimensiones(self):
        """Verifica que cada dimensión contribute al resultado"""
        respuestas = {
            'estrategia': 4,
            'gobierno': 3,
            'tecnologia': 5,
            'procesos': 2,
            'personas': 4,
            'cultura': 3
        }
        resultado = evaluar_madurez_deltha(respuestas)
        assert 'puntuacion' in resultado
        assert 'puntuaciones_dimension' in resultado


class TestCalculoPuntuacionGlobal:
    """Pruebas para el cálculo de puntuación integrada"""
    
    def test_calculo_puntuacion_global_pesos_iguales(self):
        """Verifica el cálculo con pesos iguales"""
        resultado_gartner = {'nivel': 3, 'puntuacion': 3.0}
        resultado_deltha = {'nivel': 3, 'puntuacion': 3.0}
        
        global_score = calcular_puntuacion_global(resultado_gartner, resultado_deltha)
        assert 0 <= global_score <= 5
    
    def test_calculo_puntuacion_global_pesos_diferentes(self):
        """Verifica el cálculo con pesos自定义"""
        resultado_gartner = {'nivel': 4, 'puntuacion': 4.0}
        resultado_deltha = {'nivel': 2, 'puntuacion': 2.0}
        
        global_score = calcular_puntuacion_global(resultado_gartner, resultado_deltha, peso_gartner=0.7, peso_deltha=0.3)
        assert 0 <= global_score <= 5
    
    def test_calculo_puntuacion_global_suma_pesos(self):
        """Verifica que los pesos sumen 1"""
        resultado_gartner = {'nivel': 3, 'puntuacion': 3.0}
        resultado_deltha = {'nivel': 3, 'puntuacion': 3.0}
        
        with pytest.raises(ValueError):
            calcular_puntuacion_global(resultado_gartner, resultado_deltha, peso_gartner=0.5, peso_deltha=0.3)


class TestGenerarInformeEvaluacion:
    """Pruebas para la generación de informes"""
    
    def test_generar_informe_evaluacion_formato_json(self):
        """Verifica que el informe se genera en formato JSON"""
        respuestas_gartner = {
            'datos_disponibles': 3,
            'analisis_basico': 3,
            'toma_decisiones': 3,
            'optimizacion': 3,
            'predictivo': 3
        }
        respuestas_deltha = {
            'estrategia': 3,
            'gobierno': 3,
            'tecnologia': 3,
            'procesos': 3,
            'personas': 3,
            'cultura': 3
        }
        
        informe = generar_informe_evaluacion(respuestas_gartner, respuestas_deltha)
        assert isinstance(informe, dict)
        assert 'gartner' in informe
        assert 'deltha' in informe
        assert 'puntuacion_global' in informe
    
    def test_generar_informe_evaluacion_contiene_fecha(self):
        """Verifica que el informe incluye marca temporal"""
        respuestas_gartner = {k: 3 for k in ['datos_disponibles', 'analisis_basico', 'toma_decisiones', 'optimizacion', 'predictivo']}
        respuestas_deltha = {k: 3 for k in ['estrategia', 'gobierno', 'tecnologia', 'procesos', 'personas', 'cultura']}
        
        informe = generar_informe_evaluacion(respuestas_gartner, respuestas_deltha)
        assert 'fecha_evaluacion' in informe


class TestConstantesModelos:
    """Pruebas para las constantes definidas"""
    
    def test_niveles_gartner_tiene_5_niveles(self):
        """Verifica que Gartner tiene 5 niveles"""
        assert len(NIVELES_GARTNER) == 5
    
    def test_niveles_deltha_tiene_5_niveles(self):
        """Verifica que Deltha tiene 5 niveles"""
        assert len(NIVELES_DELTHA) == 5
    
    def test_niveles_gartner_tienen_descripcion(self):
        """Verifica que cada nivel Gartner tiene descripción"""
        for nivel, info in NIVELES_GARTNER.items():
            assert 'descripcion' in info
            assert len(info['descripcion']) > 0
    
    def test_niveles_deltha_tienen_caracteristicas(self):
        """Verifica que cada nivel Deltha tiene características"""
        for nivel, info in NIVELES_DELTHA.items():
            assert 'caracteristicas' in info
            assert len(info['caracteristicas']) > 0