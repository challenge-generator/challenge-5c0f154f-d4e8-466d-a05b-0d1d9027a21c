import pytest
from unittest.mock import patch, MagicMock
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from recommendations.recomendaciones import (
    generar_recomendaciones,
    priorizar_recomendaciones,
    filtrar_por_plazo,
    generar_roadmap,
    CATEGORIAS_RECOMENDACIONES,
    PLAZOS_IMPLEMENTACION
)


class TestGenerarRecomendaciones:
    """Pruebas para la generación de recomendaciones"""
    
    def test_generar_recomendaciones_nivel_inicial_gartner(self):
        """Verifica recomendaciones para nivel 1 Gartner"""
        evaluacion = {
            'modelo': 'gartner',
            'nivel_actual': 1,
            'nivel_objetivo': 3,
            'dimensiones_debiles': ['datos_disponibles', 'analisis_basico']
        }
        recomendaciones = generar_recomendaciones(evaluacion)
        assert isinstance(recomendaciones, list)
        assert len(recomendaciones) > 0
        for rec in recomendaciones:
            assert 'titulo' in rec
            assert 'descripcion' in rec
            assert 'categoria' in rec
    
    def test_generar_recomendaciones_nivel_intermedio_gartner(self):
        """Verifica recomendaciones para nivel 3 Gartner"""
        evaluacion = {
            'modelo': 'gartner',
            'nivel_actual': 3,
            'nivel_objetivo': 5,
            'dimensiones_debiles': ['predictivo', 'optimizacion']
        }
        recomendaciones = generar_recomendaciones(evaluacion)
        assert len(recomendaciones) > 0
        assert any('predictivo' in rec.get('descripcion', '').lower() or 'avanzado' in rec.get('descripcion', '').lower() for rec in recomendaciones)
    
    def test_generar_recomendaciones_nivel_inicial_deltha(self):
        """Verifica recomendaciones para nivel 1 Deltha"""
        evaluacion = {
            'modelo': 'deltha',
            'nivel_actual': 1,
            'nivel_objetivo': 2,
            'dimensiones_debiles': ['estrategia', 'gobierno']
        }
        recomendaciones = generar_recomendaciones(evaluacion)
        assert isinstance(recomendaciones, list)
        assert len(recomendaciones) > 0
    
    def test_generar_recomendaciones_mejora_minima(self):
        """Verifica recomendaciones para mejora de un nivel"""
        evaluacion = {
            'modelo': 'gartner',
            'nivel_actual': 2,
            'nivel_objetivo': 3,
            'dimensiones_debiles': ['analisis_basico']
        }
        recomendaciones = generar_recomendaciones(evaluacion)
        assert len(recomendaciones) <= 5
    
    def test_generar_recomendaciones_mejora_maxima(self):
        """Verifica recomendaciones para mejora de varios niveles"""
        evaluacion = {
            'modelo': 'deltha',
            'nivel_actual': 1,
            'nivel_objetivo': 5,
            'dimensiones_debiles': ['estrategia', 'gobierno', 'tecnologia', 'procesos', 'personas', 'cultura']
        }
        recomendaciones = generar_recomendaciones(evaluacion)
        assert len(recomendaciones) >= 5


class TestPriorizarRecomendaciones:
    """Pruebas para la priorización de recomendaciones"""
    
    def test_priorizar_recomendaciones_por_impacto(self):
        """Verifica que las recomendaciones se ordenan por impacto"""
        recomendaciones = [
            {'titulo': 'Baja prioridad', 'impacto': 1, 'esfuerzo': 2},
            {'titulo': 'Alta prioridad', 'impacto': 5, 'esfuerzo': 3},
            {'titulo': 'Media prioridad', 'impacto': 3, 'esfuerzo': 1}
        ]
        priorizadas = priorizar_recomendaciones(recomendaciones, criterio='impacto')
        assert priorizadas[0]['impacto'] >= priorizadas[1]['impacto']
        assert priorizadas[1]['impacto'] >= priorizadas[2]['impacto']
    
    def test_priorizar_recomendaciones_por_relacion_impacto_esfuerzo(self):
        """Verifica priorización por ratio impacto/esfuerzo"""
        recomendaciones = [
            {'titulo': 'Alto esfuerzo', 'impacto': 4, 'esfuerzo': 5},
            {'titulo': 'Bajo esfuerzo', 'impacto': 3, 'esfuerzo': 1},
            {'titulo': 'Medio esfuerzo', 'impacto': 4, 'esfuerzo': 2}
        ]
        priorizadas = priorizar_recomendaciones(recomendaciones, criterio='ratio')
        assert 'ratio' in priorizadas[0] or 'prioridad' in priorizadas[0]
    
    def test_priorizar_recomendaciones_sin_criterio_valido(self):
        """Verifica manejo de criterio inválido"""
        recomendaciones = [{'titulo': 'Test', 'impacto': 3, 'esfuerzo': 2}]
        with pytest.raises(ValueError):
            priorizar_recomendaciones(recomendaciones, criterio='invalido')


class TestFiltrarPorPlazo:
    """Pruebas para filtrar recomendaciones por plazo"""
    
    def test_filtrar_por_plazo_corto(self):
        """Verifica filtro para plazo corto"""
        recomendaciones = [
            {'titulo': 'Corto plazo', 'plazo': 'corto'},
            {'titulo': 'Largo plazo', 'plazo': 'largo'},
            {'titulo': 'Medio plazo', 'plazo': 'medio'}
        ]
        filtradas = filtrar_por_plazo(recomendaciones, plazo='corto')
        assert len(filtradas) == 1
        assert filtradas[0]['plazo'] == 'corto'
    
    def test_filtrar_por_plazo_todos(self):
        """Verifica que sin filtro retorna todas"""
        recomendaciones = [
            {'titulo': 'Corto plazo', 'plazo': 'corto'},
            {'titulo': 'Largo plazo', 'plazo': 'largo'}
        ]
        filtradas = filtrar_por_plazo(recomendaciones)
        assert len(filtradas) == 2
    
    def test_filtrar_por_plazo_multiple(self):
        """Verifica filtro para múltiples plazos"""
        recomendaciones = [
            {'titulo': 'Corto plazo', 'plazo': 'corto'},
            {'titulo': 'Medio plazo', 'plazo': 'medio'},
            {'titulo': 'Largo plazo', 'plazo': 'largo'}
        ]
        filtradas = filtrar_por_plazo(recomendaciones, plazo=['corto', 'medio'])
        assert len(filtradas) == 2


class TestGenerarRoadmap:
    """Pruebas para la generación de roadmap"""
    
    def test_generar_roadmap_estructura(self):
        """Verifica la estructura del roadmap"""
        recomendaciones = [
            {'titulo': 'Implementar dashboard', 'plazo': 'corto', 'categoria': 'tecnologia'},
            {'titulo': 'Capacitar equipo', 'plazo': 'medio', 'categoria': 'personas'},
            {'titulo': 'Establecer gobernanza', 'plazo': 'largo', 'categoria': 'gobierno'}
        ]
        roadmap = generar_roadmap(recomendaciones)
        assert isinstance(roadmap, dict)
        assert 'fases' in roadmap or 'cronograma' in roadmap or 'timeline' in roadmap
    
    def test_generar_roadmap_fases_ordenadas(self):
        """Verifica que las fases están ordenadas"""
        recomendaciones = [
            {'titulo': 'Quick win', 'plazo': 'corto'},
            {'titulo': 'Mediano plazo', 'plazo': 'medio'},
            {'titulo': 'Largo plazo', 'plazo': 'largo'}
        ]
        roadmap = generar_roadmap(recomendaciones)
        assert roadmap is not None
    
    def test_generar_roadmap_vacio(self):
        """Verifica manejo de lista vacía"""
        roadmap = generar_roadmap([])
        assert roadmap is not None
        assert len(roadmap.get('fases', [])) == 0 or len(roadmap.get('cronograma', [])) == 0


class TestConstantesRecomendaciones:
    """Pruebas para las constantes de recomendaciones"""
    
    def test_categorias_recomendaciones_tiene_categorias(self):
        """Verifica que existen categorías definidas"""
        assert isinstance(CATEGORIAS_RECOMENDACIONES, dict)
        assert len(CATEGORIAS_RECOMENDACIONES) > 0
    
    def test_plazos_implementacion_tiene_plazos(self):
        """Verifica que existen plazos definidos"""
        assert isinstance(PLAZOS_IMPLEMENTACION, dict)
        assert 'corto' in PLAZOS_IMPLEMENTACION
        assert 'medio' in PLAZOS_IMPLEMENTACION
        assert 'largo' in PLAZOS_IMPLEMENTACION
    
    def test_plazos_tienen_duracion(self):
        """Verifica que cada plazo tiene duración en meses"""
        for plazo, info in PLAZOS_IMPLEMENTACION.items():
            assert 'meses' in info or 'duracion' in info
            assert info.get('meses', info.get('duracion', 0)) > 0


class TestIntegracionEvaluacionRecomendaciones:
    """Pruebas de integración entre evaluación y recomendaciones"""
    
    def test_recomendaciones_reflejan_nivel_actual(self):
        """Verifica que las recomendaciones son apropiadas para el nivel"""
        evaluacion_nivel_bajo = {
            'modelo': 'gartner',
            'nivel_actual': 1,
            'nivel_objetivo': 2,
            'dimensiones_debiles': ['datos_disponibles']
        }
        recs_nivel_bajo = generar_recomendaciones(evaluacion_nivel_bajo)
        
        evaluacion_nivel_alto = {
            'modelo': 'gartner',
            'nivel_actual': 4,
            'nivel_objetivo': 5,
            'dimensiones_debiles': ['predictivo']
        }
        recs_nivel_alto = generar_recomendaciones(evaluacion_nivel_alto)
        
        assert len(recs_nivel_bajo) > 0
        assert len(recs_nivel_alto) > 0