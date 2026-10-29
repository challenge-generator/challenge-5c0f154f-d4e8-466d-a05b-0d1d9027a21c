"""
Módulo de recomendaciones para mejorar la madurez analítica.
Genera sugerencias específicas basadas en la evaluación de madurez
utilizando los Modelos de Gartner y Deltha.
"""

from typing import Any
from dataclasses import dataclass
from enum import Enum


class NivelMadurez(str, Enum):
    """Niveles de madurez analítica según Gartner."""
    NIVEL_1_INICIAL = "1- Inicial"
    NIVEL_2_GESTIONADO = "2- Gestionado"
    NIVEL_3_DEFINIDO = "3- Definido"
    NIVEL_4_CUANTIFICATIVO = "4- Cuantitativo"
    NIVEL_5_OPTIMIZADO = "5- Optimizado"


@dataclass
class DimensionMadurez:
    """Representa una dimensión de madurez analítica."""
    nombre: str
    puntuacion_actual: float
    puntuacion_maxima: float
    peso: float

    @property
    def porcentaje(self) -> float:
        """Calcula el porcentaje de madurez de la dimensión."""
        if self.puntuacion_maxima == 0:
            return 0.0
        return (self.puntuacion_actual / self.puntuacion_maxima) * 100


@dataclass
class Recomendacion:
    """Representa una recomendación para mejorar la madurez."""
    dimension: str
    nivel_actual: str
    nivel_objetivo: str
    acciones: list[str]
    prioridad: str
    impacto_esperado: str


class GeneradorRecomendaciones:
    """
    Generador de recomendaciones para mejorar la madurez analítica.
    Analiza el estado actual y sugiere acciones específicas por dimensión.
    """

    def __init__(self):
        self.acciones_por_nivel = self._inicializar_acciones()

    def _inicializar_acciones(self) -> dict[str, dict[str, list[str]]]:
        """Inicializa el mapa de acciones por nivel y dimensión."""
        return {
            "1- Inicial": {
                "datos": [
                    "Establecer un inventario centralizado de fuentes de datos",
                    "Definir estándares básicos de calidad de datos",
                    "Implementar procesos manuales de validación"
                ],
                "tecnologia": [
                    "Evaluar herramientas de almacenamiento disponibles",
                    "Configurar entornos de desarrollo y pruebas",
                    "Establecer políticas básicas de seguridad"
                ],
                "procesos": [
                    "Documentar los procesos analíticos actuales",
                    "Identificar stakeholders clave para datos",
                    "Crear un comité de datos básico"
                ],
                "personas": [
                    "Capacitar en conceptos básicos de datos",
                    "Asignar responsables de datos por área",
                    "Establecer comunicación entre áreas técnicas"
                ],
                "governance": [
                    "Definir propietario de datos por sistema",
                    "Establecer políticas básicas de acceso",
                    "Crear proceso de solicitud de datos"
                ]
            },
            "2- Gestionado": {
                "datos": [
                    "Implementar catálogo de datos corporativo",
                    "Establecer métricas de calidad automáticas",
                    "Definir SLAs para disponibilidad de datos"
                ],
                "tecnologia": [
                    "Implementar pipeline de datos automatizado",
                    "Adoptar herramientas de visualización estándar",
                    "Configurar entornos de producción"
                ],
                "procesos": [
                    "Estandarizar procesos de reporting",
                    "Definir flujos de trabajo analíticos",
                    "Establecer ciclos de publicación de insights"
                ],
                "personas": [
                    "Formar equipo dedicado de datos",
                    "Desarrollar competencias analíticas avanzadas",
                    "Crear comunidad de práctica de datos"
                ],
                "governance": [
                    "Implementar marco de governance formal",
                    "Establecer políticas de retención de datos",
                    "Definir proceso de gestión de cambios"
                ]
            },
            "3- Definido": {
                "datos": [
                    "Implementar arquitectura de datos enterprise",
                    "Establecer linaje de datos completo",
                    "Automatizar detección de anomalías"
                ],
                "tecnologia": [
                    "Adoptar plataforma de datos moderna (Data Lake/Lakehouse)",
                    "Implementar herramientas de MLops",
                    "Configurar entornos de experimentación"
                ],
                "procesos": [
                    "Estandarizar metodología de proyectos analíticos",
                    "Implementar proceso de gestión de modelos",
                    "Establecer métricas de negocio para proyectos"
                ],
                "personas": [
                    "Expandir equipo con roles especializados",
                    "Desarrollar programa de citizen data scientists",
                    "Establecer carrera profesional en datos"
                ],
                "governance": [
                    "Implementar Data Catalog enterprise",
                    "Establecer políticas de datos automatizadas",
                    "Crear центр компетенций (centro de excelencia)"
                ]
            },
            "4- Cuantitativo": {
                "datos": [
                    "Implementar observabilidad de datos completa",
                    "Establecer métricas de calidad en tiempo real",
                    "Automatizar gobernanza basada en políticas"
                ],
                "tecnologia": [
                    "Adoptar arquitectura de datos en tiempo real",
                    "Implementar A/B testing automatizado",
                    "Configurar MLOps enterprise"
                ],
                "procesos": [
                    "Implementar gestión de decisiones basada en datos",
                    "Establecer procesos de mejora continua",
                    "Medir ROI de iniciativas analíticas"
                ],
                "personas": [
                    "Desarrollar cultura data-driven organizacional",
                    "Establecer métricas de alfabetización de datos",
                    "Crear incentivos por uso de datos"
                ],
                "governance": [
                    "Implementar stewardship automatizado",
                    "Establecer compliance automatizado",
                    "Crear métricas de gobierno effectiveness"
                ]
            },
            "5- Optimizado": {
                "datos": [
                    "Innovar con datos sintéticos y augmentación",
                    "Implementar arquitectura de datos autónoma",
                    "Establecer partnerships de datos externos"
                ],
                "tecnologia": [
                    "Adoptar IA generativa para operaciones de datos",
                    "Implementar compute everywhere (edge, cloud, on-prem)",
                    "Configurar auto-healing de pipelines"
                ],
                "procesos": [
                    "Innovar continuamente procesos analíticos",
                    "Establecer labs de innovación en datos",
                    "Crear ecosistema de datos abierto"
                ],
                "personas": [
                    "Desarrollar thought leaders en datos",
                    "Crear comunidad de práctica global",
                    "Establecer programas de investigación"
                ],
                "governance": [
                    "Implementar governance predictivo",
                    "Establecer ética de datos avanzada",
                    "Crear estándares de industria"
                ]
            }
        }

    def generar_recomendaciones(
        self,
        dimensiones: list[DimensionMadurez],
        nivel_actual: str
    ) -> list[Recomendacion]:
        """
        Genera recomendaciones basadas en las dimensiones evaluadas.

        Args:
            dimensiones: Lista de dimensiones de madurez evaluadas
            nivel_actual: Nivel de madurez actual según Gartner

        Returns:
            Lista de recomendaciones priorizadas
        """
        recomendaciones = []
        nivel_idx = self._obtener_indice_nivel(nivel_actual)

        for dim in dimensiones:
            if dim.porcentaje < 70:
                acciones = self._obtener_acciones_dimension(
                    dim.nombre, nivel_actual
                )
                prioridad = self._calcular_prioridad(dim.porcentaje)
                impacto = self._estimar_impacto(dim.nombre, dim.porcentaje)

                nivel_objetivo = self._sugerir_nivel_objetivo(
                    nivel_idx, dim.porcentaje
                )

                recomendaciones.append(
                    Recomendacion(
                        dimension=dim.nombre,
                        nivel_actual=nivel_actual,
                        nivel_objetivo=nivel_objetivo,
                        acciones=acciones,
                        prioridad=prioridad,
                        impacto_esperado=impacto
                    )
                )

        return sorted(
            recomendaciones,
            key=lambda r: self._ponderar_prioridad(r.prioridad),
            reverse=True
        )

    def _obtener_indice_nivel(self, nivel: str) -> int:
        """Obtiene el índice numérico del nivel de madurez."""
        niveles = [n.value for n in NivelMadurez]
        try:
            return niveles.index(nivel)
        except ValueError:
            return 0

    def _obtener_acciones_dimension(
        self,
        dimension: str,
        nivel_actual: str
    ) -> list[str]:
        """Obtiene las acciones recomendadas para una dimensión y nivel."""
        nivel_key = nivel_actual.split("-")[0].strip() + "- " + nivel_actual.split("-")[1].strip() if "-" in nivel_actual else nivel_actual

        if nivel_key in self.acciones_por_nivel:
            dim_key = dimension.lower()
            if dim_key in self.acciones_por_nivel[nivel_key]:
                return self.acciones_por_nivel[nivel_key][dim_key].copy()

        return self.acciones_por_nivel.get(
            "1- Inicial", {}
        ).get(dimension.lower(), [
            "Consultar con experto en madurez analítica"
        ])

    def _calcular_prioridad(self, porcentaje: float) -> str:
        """Calcula la prioridad basada en el porcentaje de madurez."""
        if porcentaje < 30:
            return "CRÍTICA"
        elif porcentaje < 50:
            return "ALTA"
        elif porcentaje < 70:
            return "MEDIA"
        else:
            return "BAJA"

    def _estimar_impacto(self, dimension: str, porcentaje: float) -> str:
        """Estima el impacto esperado de mejorar la dimensión."""
        impacto_base = {
            "datos": "Mejora en la calidad de decisiones hasta un 40%",
            "tecnologia": "Reducción de costos operativos hasta un 25%",
            "procesos": "Aumento de eficiencia hasta un 35%",
            "personas": "Incremento de productividad hasta un 30%",
            "governance": "Reducción de riesgos hasta un 50%"
        }

        base = impacto_base.get(
            dimension.lower(),
            "Mejora significativa en capacidades analíticas"
        )

        if porcentaje < 30:
            return f"MUY ALTO: {base}"
        elif porcentaje < 50:
            return f"ALTO: {base}"
        else:
            return f"MODERADO: {base}"

    def _sugerir_nivel_objetivo(
        self,
        nivel_idx: int,
        porcentaje_actual: float
    ) -> str:
        """Sugiere un nivel objetivo realista."""
        if porcentaje_actual < 30 and nivel_idx < 2:
            return "2- Gestionado"
        elif porcentaje_actual < 50 and nivel_idx < 3:
            return "3- Definido"
        elif porcentaje_actual < 70 and nivel_idx < 4:
            return "4- Cuantitativo"
        else:
            niveles = [n.value for n in NivelMadurez]
            siguiente = min(nivel_idx + 1, len(niveles) - 1)
            return niveles[siguiente]

    def _ponderar_prioridad(self, prioridad: str) -> int:
        """Convierte prioridad textual a valor numérico para ordenamiento."""
        ponderacion = {
            "CRÍTICA": 4,
            "ALTA": 3,
            "MEDIA": 2,
            "BAJA": 1
        }
        return ponderacion.get(prioridad, 0)

    def generar_roadmap(
        self,
        recomendaciones: list[Recomendacion],
        horizonte_tiempo: int = 12
    ) -> dict[str, list[str]]:
        """
        Genera un roadmap de implementación por trimestre.

        Args:
            recomendaciones: Lista de recomendaciones a implementar
            horizonte_tiempo: Horizonte de planificación en meses

        Returns:
            Roadmap con acciones por trimestre
        """
        roadmap = {
            "Q1 (0-3 meses)": [],
            "Q2 (3-6 meses)": [],
            "Q3 (6-9 meses)": [],
            "Q4 (9-12 meses)": []
        }

        for rec in recomendaciones[:10]:
            if rec.prioridad == "CRÍTICA":
                roadmap["Q1 (0-3 meses)"].extend(
                    rec.acciones[:2]
                )
            elif rec.prioridad == "ALTA":
                roadmap["Q2 (3-6 meses)"].extend(
                    rec.acciones[:2]
                )
            elif rec.prioridad == "MEDIA":
                roadmap["Q3 (6-9 meses)"].extend(
                    rec.acciones[:1]
                )
            else:
                roadmap["Q4 (9-12 meses)"].extend(
                    rec.acciones[:1]
                )

        return {k: v for k, v in roadmap.items() if v}

    def calcular_score_general(
        self,
        dimensiones: list[DimensionMadurez]
    ) -> dict[str, Any]:
        """
        Calcula un score general de madurez ponderado.

        Args:
            dimensiones: Lista de dimensiones evaluadas

        Returns:
            Diccionario con score y desglose por dimensión
        """
        if not dimensiones:
            return {
                "score_general": 0.0,
                "nivel_gartner": "1- Inicial",
                "detalle": {}
            }

        peso_total = sum(d.peso for d in dimensiones)
        score_ponderado = sum(
            d.porcentaje * d.peso for d in dimensiones
        ) / peso_total if peso_total > 0 else 0

        nivel_gartner = self._determinar_nivel_gartner(score_ponderado)

        return {
            "score_general": round(score_ponderado, 2),
            "nivel_gartner": nivel_gartner,
            "detalle": {
                d.nombre: {
                    "puntuacion": round(d.porcentaje, 2),
                    "peso": d.peso,
                    "puntuacion_ponderada": round(
                        d.porcentaje * d.peso, 2
                    )
                }
                for d in dimensiones
            }
        }

    def _determinar_nivel_gartner(self, score: float) -> str:
        """Determina el nivel Gartner basado en el score."""
        if score < 20:
            return "1- Inicial"
        elif score < 40:
            return "2- Gestionado"
        elif score < 60:
            return "3- Definido"
        elif score < 80:
            return "4- Cuantitativo"
        else:
            return "5- Optimizado"


def generar_recomendaciones_rapidas(
    nivel_actual: str,
    dimensiones_debiles: list[str]
) -> dict[str, list[str]]:
    """
    Función de conveniencia para generar recomendaciones rápidas.

    Args:
        nivel_actual: Nivel de madurez actual
        dimensiones_debiles: Lista de dimensiones con bajo rendimiento

    Returns:
    Diccionario de recomendaciones por dimensión
    """
    generador = GeneradorRecomendaciones()
    dims = [
        DimensionMadurez(
            nombre=d,
            puntuacion_actual=30.0,
            puntuacion_maxima=100.0,
            peso=1.0
        )
        for d in dimensiones_debiles
    ]

    recomendaciones = generador.generar_recomendaciones(dims, nivel_actual)

    return {
        r.dimension: r.acciones for r in recomendaciones
    }