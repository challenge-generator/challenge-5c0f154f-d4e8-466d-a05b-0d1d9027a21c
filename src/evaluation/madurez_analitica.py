"""
Módulo de evaluación de madurez analítica basado en Modelos de Gartner y Deltha.
Proporciona herramientas para evaluar el nivel de madurez de una organización
y generar recomendaciones de mejora.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any
import json


class NivelMadurez(Enum):
    """Enumeración de niveles de madurez analítica."""
    NIVEL_1_BASICO = "Nivel 1 - Básico"
    NIVEL_2_TRANSACCIONAL = "Nivel 2 - Transaccional"
    NIVEL_3_AVANZADO = "Nivel 3 - Avanzado"
    NIVEL_4_ESTRATEGICO = "Nivel 4 - Estratégico"
    NIVEL_5_TRANSFORMADOR = "Nivel 5 - Transformador"


@dataclass
class CriterioEvaluacion:
    """Representa un criterio individual de evaluación de madurez."""
    nombre: str
    descripcion: str
    peso: float
    puntuacion_actual: float = 0.0
    evidencia: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not 0.0 <= self.puntuacion_actual <= 10.0:
            raise ValueError("La puntuación debe estar entre 0 y 10")
        if not 0.0 <= self.peso <= 1.0:
            raise ValueError("El peso debe estar entre 0 y 1")

    def puntuacion_ponderada(self) -> float:
        """Calcula la puntuación ponderada del criterio."""
        return self.puntuacion_actual * self.peso


@dataclass
class DimensionMadurez:
    """Agrupa criterios relacionados en una dimensión de madurez."""
    nombre: str
    descripcion: str
    criterios: list[CriterioEvaluacion]

    def puntuacion_total(self) -> float:
        """Calcula la puntuación ponderada total de la dimensión."""
        return sum(c.puntuacion_ponderada() for c in self.criterios)

    def peso_total(self) -> float:
        """Retorna el peso total de los criterios en la dimensión."""
        return sum(c.peso for c in self.criterios)


@dataclass
class ResultadoEvaluacion:
    """Almacena el resultado completo de una evaluación de madurez."""
    nivel_gartner: NivelMadurez
    nivel_deltha: NivelMadurez
    puntuacion_gartner: float
    puntuacion_deltha: float
    dimensiones: list[DimensionMadurez]
    fortalezas: list[str] = field(default_factory=list)
    debilidades: list[str] = field(default_factory=list)
    recomendaciones: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convierte el resultado a un diccionario serializable."""
        return {
            "nivel_gartner": self.nivel_gartner.value,
            "nivel_deltha": self.nivel_deltha.value,
            "puntuacion_gartner": round(self.puntuacion_gartner, 2),
            "puntuacion_deltha": round(self.puntuacion_deltha, 2),
            "fortalezas": self.fortalezas,
            "debilidades": self.debilidades,
            "recomendaciones": self.recomendaciones,
            "dimensiones": [
                {
                    "nombre": d.nombre,
                    "puntuacion": round(d.puntuacion_total(), 2),
                    "criterios": [
                        {
                            "nombre": c.nombre,
                            "puntuacion": c.puntuacion_actual,
                            "ponderada": round(c.puntuacion_ponderada(), 2)
                        }
                        for c in d.criterios
                    ]
                }
                for d in self.dimensiones
            ]
        }


class ModeloGartner:
    """
    Implementación del Modelo de Madurez Analítica de Gartner.
    Este modelo evalúa la capacidad analítica de una organización
    en cinco niveles progresivos.
    """

    def __init__(self):
        self.niveles = {
            1: {
                "nombre": NivelMadurez.NIVEL_1_BASICO,
                "descripcion": "Reporting básico y hojas de cálculo",
                "caracteristicas": [
                    "Análisis retrospectivo",
                    "Reportes estáticos",
                    "Decisiones basadas en intuición"
                ],
                "tecnologias": ["Excel", "Reporting básico"]
            },
            2: {
                "nombre": NivelMadurez.NIVEL_2_TRANSACCIONAL,
                "descripcion": "Análisis descriptivo y dashboards",
                "caracteristicas": [
                    "Dashboards en tiempo real",
                    "Análisis de tendencias",
                    "KPIs definidos"
                ],
                "tecnologias": ["BI tradicional", "ETL básico"]
            },
            3: {
                "nombre": NivelMadurez.NIVEL_3_AVANZADO,
                "descripcion": "Análisis predictivo y modelos estadísticos",
                "caracteristicas": [
                    "Modelos predictivos",
                    "Segmentación avanzada",
                    "Análisis de escenarios"
                ],
                "tecnologias": ["ML", "Python/R", "Data Warehouses"]
            },
            4: {
                "nombre": NivelMadurez.NIVEL_4_ESTRATEGICO,
                "descripcion": "Análisis prescriptivo y optimización",
                "caracteristicas": [
                    "Optimización de decisiones",
                    "Modelos prescriptivos",
                    "Integración con procesos de negocio"
                ],
                "tecnologias": ["Prescriptive Analytics", "OR-Tools"]
            },
            5: {
                "nombre": NivelMadurez.NIVEL_5_TRANSFORMADOR,
                "descripcion": "IA avanzada y decisiones autónomas",
                "caracteristicas": [
                    "Decisiones autonomous",
                    "IA generativa",
                    "Transformación digital completa"
                ],
                "tecnologias": ["AI/ML avanzado", "AutoML"]
            }
        }

    def crear_criterios_default(self) -> list[DimensionMadurez]:
        """Crea las dimensiones y criterios estándar del modelo Gartner."""
        return [
            DimensionMadurez(
                nombre="Cultura de Datos",
                descripcion="Grado de adopción de una cultura basada en datos",
                criterios=[
                    CriterioEvaluacion(
                        nombre="Data-driven decision making",
                        descripcion="Las decisiones se basan en evidencia analítica",
                        peso=0.4
                    ),
                    CriterioEvaluacion(
                        nombre="Literacia de datos",
                        descripcion="Capacidad del personal para interpretar datos",
                        peso=0.3
                    ),
                    CriterioEvaluacion(
                        nombre="Gobernanza de datos",
                        descripcion="Políticas y procesos de gestión de datos",
                        peso=0.3
                    )
                ]
            ),
            DimensionMadurez(
                nombre="Infraestructura Tecnológica",
                descripcion="Capacidad de la infraestructura de datos",
                criterios=[
                    CriterioEvaluacion(
                        nombre="Calidad de datos",
                        descripcion="Completitud, precisión y consistencia de datos",
                        peso=0.35
                    ),
                    CriterioEvaluacion(
                        nombre="Disponibilidad",
                        descripcion="Acceso oportuno a los datos necesarios",
                        peso=0.35
                    ),
                    CriterioEvaluacion(
                        nombre="Integración",
                        descripcion="Capacidad de integrar fuentes de datos",
                        peso=0.30
                    )
                ]
            ),
            DimensionMadurez(
                nombre="Capacidad Analítica",
                descripcion="Habilidades y herramientas para análisis avanzado",
                criterios=[
                    CriterioEvaluacion(
                        nombre="Análisis descriptivo",
                        descripcion="Capacidad de entender qué sucedió",
                        peso=0.25
                    ),
                    CriterioEvaluacion(
                        nombre="Análisis predictivo",
                        descripcion="Capacidad de predecir qué sucederá",
                        peso=0.35
                    ),
                    CriterioEvaluacion(
                        nombre="Análisis prescriptivo",
                        descripcion="Capacidad de recomendar acciones",
                        peso=0.40
                    )
                ]
            )
        ]

    def determinar_nivel(self, puntuacion: float) -> NivelMadurez:
        """Determina el nivel de madurez según la puntuación (0-10)."""
        if puntuacion < 2:
            return NivelMadurez.NIVEL_1_BASICO
        elif puntuacion < 4:
            return NivelMadurez.NIVEL_2_TRANSACCIONAL
        elif puntuacion < 6:
            return NivelMadurez.NIVEL_3_AVANZADO
        elif puntuacion < 8:
            return NivelMadurez.NIVEL_4_ESTRATEGICO
        else:
            return NivelMadurez.NIVEL_5_TRANSFORMADOR

    def caracteristicas_del_nivel(self, nivel: int) -> dict[str, Any]:
        """Retorna las características del nivel especificado."""
        return self.niveles.get(nivel, {})


class ModeloDeltha:
    """
    Implementación del Modelo Deltha de madurez analítica.
    Este modelo evalúa la transformación hacia una organización
    dirigida por datos con enfoque en dimensiones específicas.
    """

    def __init__(self):
        self.niveles = {
            1: {
                "nombre": NivelMadurez.NIVEL_1_BASICO,
                "descripcion": "Organización reactiva",
                "caracteristicas": [
                    "Sin estrategia de datos",
                    "Datos aislados en silos",
                    "Decisiones políticas/intuitivas"
                ],
                "madurez_datos": "Baja"
            },
            2: {
                "nombre": NivelMadurez.NIVEL_2_TRANSACCIONAL,
                "descripcion": "Organización consciente",
                "caracteristicas": [
                    "Estrategia de datos emergente",
                    "Iniciativas de BI aisladas",
                    "Reporting regular"
                ],
                "madurez_datos": "Media-baja"
            },
            3: {
                "nombre": NivelMadurez.NIVEL_3_AVANZADO,
                "descripcion": "Organización impulsada por datos",
                "caracteristicas": [
                    "Estrategia de datos formalizada",
                    "Data warehouse operativo",
                    "Analytics para optimización"
                ],
                "madurez_datos": "Media"
            },
            4: {
                "nombre": NivelMadurez.NIVEL_4_ESTRATEGICO,
                "descripcion": "Organización basada en datos",
                "caracteristicas": [
                    "Datos como activo estratégico",
                    "ML en producción",
                    "Decisiones data-driven"
                ],
                "madurez_datos": "Media-alta"
            },
            5: {
                "nombre": NivelMadurez.NIVEL_5_TRANSFORMADOR,
                "descripcion": "Organización dirigida por datos",
                "caracteristicas": [
                    "Transformación cultural completa",
                    "IA en el núcleo del negocio",
                    "Innovación basada en datos"
                ],
                "madurez_datos": "Alta"
            }
        }

    def crear_criterios_default(self) -> list[DimensionMadurez]:
        """Crea las dimensiones y criterios estándar del modelo Deltha."""
        return [
            DimensionMadurez(
                nombre="Estrategia y Liderazgo",
                descripcion="Grado de compromiso ejecutivo con los datos",
                criterios=[
                    CriterioEvaluacion(
                        nombre="Visión de datos",
                        descripcion="Executive sponsorship y visión clara",
                        peso=0.35
                    ),
                    CriterioEvaluacion(
                        nombre="Inversión",
                        descripcion="Recursos dedicados a capacidades de datos",
                        peso=0.30
                    ),
                    CriterioEvaluacion(
                        nombre="Accountability",
                        descripcion="Responsabilidad clara por resultados de datos",
                        peso=0.35
                    )
                ]
            ),
            DimensionMadurez(
                nombre="Procesos y Métodos",
                descripcion="Madurez de los procesos de gestión de datos",
                criterios=[
                    CriterioEvaluacion(
                        nombre="Gestión de datos",
                        descripcion="Políticas y procesos establecidos",
                        peso=0.40
                    ),
                    CriterioEvaluacion(
                        nombre="Desarrollo analítico",
                        descripcion="Metodologías de desarrollo de modelos",
                        peso=0.30
                    ),
                    CriterioEvaluacion(
                        nombre="Operaciones",
                        descripcion="Monitoreo y mantenimiento de modelos",
                        peso=0.30
                    )
                ]
            ),
            DimensionMadurez(
                nombre="Personas y Organización",
                descripcion="Capacidades y estructura organizacional",
                criterios=[
                    CriterioEvaluacion(
                        nombre="Talento",
                        descripcion="Disponibilidad de perfiles técnicos",
                        peso=0.35
                    ),
                    CriterioEvaluacion(
                        nombre="Formación",
                        descripcion="Programas de upskilling",
                        peso=0.30
                    ),
                    CriterioEvaluacion(
                        nombre="Estructura",
                        descripcion="Organización del equipo de datos",
                        peso=0.35
                    )
                ]
            ),
            DimensionMadurez(
                nombre="Tecnología",
                descripcion="Infraestructura y herramientas",
                criterios=[
                    CriterioEvaluacion(
                        nombre="Plataforma de datos",
                        descripcion="Arquitectura de datos moderna",
                        peso=0.40
                    ),
                    CriterioEvaluacion(
                        nombre="Herramientas analíticas",
                        descripcion="Stack tecnológico avanzado",
                        peso=0.30
                    ),
                    CriterioEvaluacion(
                        nombre="Automatización",
                        descripcion="MLOps y CI/CD para datos",
                        peso=0.30
                    )
                ]
            )
        ]

    def determinar_nivel(self, puntuacion: float) -> NivelMadurez:
        """Determina el nivel de madurez según la puntuación (0-10)."""
        if puntuacion < 2:
            return NivelMadurez.NIVEL_1_BASICO
        elif puntuacion < 4:
            return NivelMadurez.NIVEL_2_TRANSACCIONAL
        elif puntuacion < 6:
            return NivelMadurez.NIVEL_3_AVANZADO
        elif puntuacion < 8:
            return NivelMadurez.NIVEL_4_ESTRATEGICO
        else:
            return NivelMadurez.NIVEL_5_TRANSFORMADOR

    def caracteristicas_del_nivel(self, nivel: int) -> dict[str, Any]:
        """Retorna las características del nivel especificado."""
        return self.niveles.get(nivel, {})


class EvaluadorMadurez:
    """
    Clase principal para evaluar la madurez analítica de una organización.
    Combina el Modelo Gartner y el Modelo Deltha para proporcionar
    una evaluación comprehensiva.
    """

    def __init__(self):
        self.modelo_gartner = ModeloGartner()
        self.modelo_deltha = ModeloDeltha()

    def cargar_datos_ejemplo(self, ruta: str) -> dict[str, Any]:
        """Carga datos de evaluación desde un archivo JSON."""
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al parsear JSON: {e}")

    def evaluar_organizacion(
        self,
        datos_evaluacion: dict[str, Any]
    ) -> ResultadoEvaluacion:
        """
        Evalúa la madurez analítica de una organización.
        
        Args:
            datos_evaluacion: Diccionario con las puntuaciones de cada criterio
        
        Returns:
            ResultadoEvaluacion con el diagnóstico completo
        """
        dimensiones_gartner = self.modelo_gartner.crear_criterios_default()
        dimensiones_deltha = self.modelo_deltha.crear_criterios_default()

        self._aplicar_puntuaciones(dimensiones_gartner, datos_evaluacion)
        self._aplicar_puntuaciones(dimensiones_deltha, datos_evaluacion)

        puntuacion_gartner = self._calcular_puntuacion_total(dimensiones_gartner)
        puntuacion_deltha = self._calcular_puntuacion_total(dimensiones_deltha)

        nivel_gartner = self.modelo_gartner.determinar_nivel(puntuacion_gartner)
        nivel_deltha = self.modelo_deltha.determinar_nivel(puntuacion_deltha)

        fortalezas = self._identificar_fortalezas(dimensiones_gartner, dimensiones_deltha)
        debilidades = self._identificar_debilidades(dimensiones_gartner, dimensiones_deltha)
        recomendaciones = self._generar_recomendaciones(
            nivel_gartner, nivel_deltha, fortalezas, debilidades
        )

        return ResultadoEvaluacion(
            nivel_gartner=nivel_gartner,
            nivel_deltha=nivel_deltha,
            puntuacion_gartner=puntuacion_gartner,
            puntuacion_deltha=puntuacion_deltha,
            dimensiones=dimensiones_gartner,
            fortalezas=fortalezas,
            debilidades=debilidades,
            recomendaciones=recomendaciones
        )

    def _aplicar_puntuaciones(
        self,
        dimensiones: list[DimensionMadurez],
        datos: dict[str, Any]
    ) -> None:
        """Aplica las puntuaciones a los criterios desde los datos de evaluación."""
        for dimension in dimensiones:
            dimension_key = dimension.nombre.lower().replace(" ", "_")
            if dimension_key in datos:
                dimension_data = datos[dimension_key]
                for criterio in dimension.criterios:
                    criterio_key = criterio.nombre.lower().replace(" ", "_")
                    if criterio_key in dimension_data:
                        criterio.puntuacion_actual = float(dimension_data[criterio_key])
                        if "evidencia" in dimension_data:
                            criterio.evidencia = dimension_data["evidencia"]

    def _calcular_puntuacion_total(self, dimensiones: list[DimensionMadurez]) -> float:
        """Calcula la puntuación total ponderada de las dimensiones."""
        puntuacion_total = sum(d.puntuacion_total() for d in dimensiones)
        peso_total = sum(d.peso_total() for d in dimensiones)
        return (puntuacion_total / peso_total * 10) if peso_total > 0 else 0.0

    def _identificar_fortalezas(
        self,
        dimensiones_gartner: list[DimensionMadurez],
        dimensiones_deltha: list[DimensionMadurez]
    ) -> list[str]:
        """Identifica las fortalezas de la organización."""
        fortalezas = []
        for dimension in dimensiones_gartner + dimensiones_deltha:
            for criterio in dimension.criterios:
                if criterio.puntuacion_actual >= 7.0:
                    fortalezas.append(
                        f"{criterio.nombre} ({dimension.nombre}): {criterio.puntuacion_actual}/10"
                    )
        return fortalezas[:5]

    def _identificar_debilidades(
        self,
        dimensiones_gartner: list[DimensionMadurez],
        dimensiones_deltha: list[DimensionMadurez]
    ) -> list[str]:
        """Identifica las debilidades de la organización."""
        debilidades = []
        for dimension in dimensiones_gartner + dimensiones_deltha:
            for criterio in dimension.criterios:
                if criterio.puntuacion_actual < 4.0:
                    debilidades.append(
                        f"{criterio.nombre} ({dimension.nombre}): {criterio.puntuacion_actual}/10"
                    )
        return debilidades[:5]

    def _generar_recomendaciones(
        self,
        nivel_gartner: NivelMadurez,
        nivel_deltha: NivelMadurez,
        fortalezas: list[str],
        debilidades: list[str]
    ) -> list[str]:
        """Genera recomendaciones basadas en la evaluación."""
        recomendaciones = []

        nivel_actual = min(
            list(NivelMadurez).index(nivel_gartner),
            list(NivelMadurez).index(nivel_deltha)
        )

        if nivel_actual < 2:
            recomendaciones.append(
                "Establecer una estrategia de datos formal con sponsorship ejecutivo"
            )
            recomendaciones.append(
                "Implementar un data warehouse para centralizar la información"
            )
            recomendaciones.append(
                "Iniciar programas de formación en literacy de datos"
            )
        elif nivel_actual < 3:
            recomendaciones.append(
                "Profesionalizar la gobernanza de datos"
            )
            recomendaciones.append(
                "Desarrollar capacidades de análisis predictivo"
            )
            recomendaciones.append(
                "Establecer KPIs y dashboards en tiempo real"
            )
        elif nivel_actual < 4:
            recomendaciones.append(
                "Implementar MLOps para operacionalizar modelos"
            )
            recomendaciones.append(
                "Desarrollar capacidades de análisis prescriptivo"
            )
            recomendaciones.append(
                "Integrar analytics en los procesos de decisión clave"
            )
        else:
            recomendaciones.append(
                "Explorar implementaciones de IA generativa"
            )
            recomendaciones.append(
                "Establecer innovación basada en datos como prioridad"
            )

        for debilidad in debilidades[:2]:
            if "predictivo" in debilidad.lower():
                recomendaciones.append(
                    "Invertir en formación de Machine Learning para el equipo"
                )
            elif "calidad" in debilidad.lower():
                recomendaciones.append(
                    "Implementar un marco de calidad de datos"
                )
            elif "gobiernan" in debilidad.lower():
                recomendaciones.append(
                    "Establecer un centro de excelencia de datos"
                )

        return recomendaciones[:6]

    def generar_informe(self, resultado: ResultadoEvaluacion) -> str:
        """Genera un informe textual de la evaluación."""
        informe = []
        informe.append("=" * 60)
        informe.append("EVALUACIÓN DE MADUREZ ANALÍTICA")
        informe.append("=" * 60)
        informe.append("")
        informe.append(f"Modelo Gartner - Nivel: {resultado.nivel_gartner.value}")
        informe.append(f"Puntuación Gartner: {resultado.puntuacion_gartner:.2f}/10")
        informe.append("")
        informe.append(f"Modelo Deltha - Nivel: {resultado.nivel_deltha.value}")
        informe.append(f"Puntuación Deltha: {resultado.puntuacion_deltha:.2f}/10")
        informe.append("")
        informe.append("-" * 60)
        informe.append("FORTALEZAS IDENTIFICADAS:")
        informe.append("-" * 60)
        for f in resultado.fortalezas:
            informe.append(f"  • {f}")
        informe.append("")
        informe.append("-" * 60)
        informe.append("DEBILIDADES IDENTIFICADAS:")
        informe.append("-" * 60)
        for d in resultado.debilidades:
            informe.append(f"  • {d}")
        informe.append("")
        informe.append("-" * 60)
        informe.append("RECOMENDACIONES:")
        informe.append("-" * 60)
        for r in resultado.recomendaciones:
            informe.append(f"  • {r}")
        informe.append("")
        informe.append("=" * 60)
        return "\n".join(informe)

    def guardar_resultado(
        self,
        resultado: ResultadoEvaluacion,
        ruta: str
    ) -> None:
        """Guarda el resultado de la evaluación en un archivo JSON."""
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(resultado.to_dict(), f, ensure_ascii=False, indent=2)