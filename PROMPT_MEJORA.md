# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Archivos que la arquitectura del reto declara y no estan

Creálos con implementacion real, en la capa que les corresponde:

- `notebooks/analisis_exploratorio_modelos.ipynb`
- `notebooks/evaluacion_madurez_actual.ipynb`
- `docs/informe_evaluacion.md`
- `docs/recomendaciones.md`

## Como saber que terminaste

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Ciencia de Datos, Especialidad Arquitecto de Datos, Senior

### Brecha de conocimiento
Conoce y experimenta los niveles de madurez de analítica (Modelo de Gartner, Modelo Deltha), características de una organización dirigida por datos. Brecha de conocimiento en evaluación de madurez analítica

### Misión / candidato
Candidato con experiencia como Arquitecto de Datos.

### Reto
- Tema: Assessment
- Seniority: senior-l2
- Tipo: theoretical
- Título: Evaluación de Madurez Analítica en una Organización Dirigida por Datos
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Exploración de Modelos de Madurez Analítica — objetivo: Comprender y comparar los Modelos de Gartner y Deltha para evaluar la madurez analítica. — entregable (NO resolver): Resumen comparativo de los Modelos de Gartner y Deltha.
- Fase 2: Evaluación de la Madurez Analítica Actual — objetivo: Aplicar los modelos para evaluar la madurez analítica actual de la organización. — entregable (NO resolver): Informe de evaluación de la madurez analítica actual de la organización.
- Fase 3: Recomendaciones para Mejorar la Madurez Analítica — objetivo: Proponer recomendaciones para avanzar en la madurez analítica de la organización. — entregable (NO resolver): Documento de recomendaciones para mejorar la madurez analítica de la organización.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: pyproject.toml ===
[build-system]
requires = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "evaluacion_madurez_analitica"
version = "0.1.0"
description = "Evaluación de madurez analítica utilizando Modelos de Gartner y Deltha"
authors = [{name = "Equipo de Datos", email = "datos@organizacion.com"}]
readme = "README.md"
requires-python = ">=3.13"
license = {text = "MIT"}

# Dependencias principales del proyecto
dependencies = [
    "pandas>=2.2.0",
    "numpy>=1.26.0",
    "matplotlib>=3.8.0",
    "scikit-learn>=1.4.0",
    "mlflow>=2.10.0",
    "jupyter>=1.0.0",
    "pytest>=8.0.0"
]

[project.optional-dependencies]
test = ["pytest-cov>=4.1.0"]
dev = ["black>=24.2.0", "flake8>=7.0.0", "mypy>=1.8.0"]

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --cov=src --cov-report=term-missing"

[tool.black]
line-length = 88
include = '\\.pyi?$'
exclude = '''
/(
    \\.git
  | \\.hg
  | \\.mypy_cache
  | \\.tox
  | \\.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''

[tool.flake8]
max-line-length = 88
ignore = ["E203", "W503"]

[tool.mypy]
python_version = "3.13"
warn_return_any = true
warn_unused_configs = true
ignore_missing_imports = true


// === ARCHIVO: src/evaluation/madurez_analitica.py ===
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


// === ARCHIVO: src/recommendations/recomendaciones.py ===
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


// === ARCHIVO: data/madurez_ejemplo.json ===
{
  "organizaciones": [
    {
      "id": "ORG-001",
      "nombre": "FinTech Solutions S.A.",
      "sector": "Financiero",
      "tamano": "Grande",
      "nivel_gartner_actual": "2- Gestionado",
      "nivel_deltha_actual": "Explorador",
      "dimensiones": {
        "datos": {
          "puntuacion": 65,
          "descripcion": "Cumplimiento parcial de calidad de datos",
          "indicadores": [
            "Inventario de datos parcial",
            "Métricas de calidad definidas",
            "Gobierno de datos básico"
          ]
        },
        "tecnologia": {
          "puntuacion": 55,
          "descripcion": "Stack tecnológico en evolución",
          "indicadores": [
            "Data warehouse operativo",
            "Pipeline de datos básicos",
            "Herramientas de BI en uso"
          ]
        },
        "procesos": {
          "puntuacion": 45,
          "descripcion": "Procesos analíticos emergentes",
          "indicadores": [
            "Reporting regular",
            "Proyectos ad-hoc",
            "Metodología en definición"
          ]
        },
        "personas": {
          "puntuacion": 40,
          "descripcion": "Equipo de datos incipiente",
          "indicadores": [
            "Equipo de 3 analistas",
            "Capacitación básica",
            "Roles no formalizados"
          ]
        },
        "governance": {
          "puntuacion": 35,
          "descripcion": "Gobernanza inicial",
          "indicadores": [
            "Política de datos básica",
            "Sin catálogo formal",
            " Stewardship parcial"
          ]
        }
      },
      "objetivo_madurez": "3- Definido",
      "prioridades": [
        "Implementar catálogo de datos",
        "Formalizar equipo de datos",
        "Estandarizar procesos analíticos"
      ]
    },
    {
      "id": "ORG-002",
      "nombre": "Retail Dynamics C.A.",
      "sector": "Comercio",
      "tamano": "Mediano",
      "nivel_gartner_actual": "1- Inicial",
      "nivel_deltha_actual": "Novato",
      "dimensiones": {
        "datos": {
          "puntuacion": 20,
          "descripcion": "Gestión de datos reactiva",
          "indicadores": [
            "Sin inventario de datos",
            "Calidad de datos no medida",
            "Sin gobierno de datos"
          ]
        },
        "tecnologia": {
          "puntuacion": 25,
          "descripcion": "Infraestructura básica",
          "indicadores": [
            "Hojas de cálculo principales",
            "Sin pipeline de datos",
            "Toolkit limitado"
          ]
        },
        "procesos": {
          "puntuacion": 15,
          "descripcion": "Procesos analíticos inexistentes",
          "indicadores": [
            "Decisiones por intuición",
            "Sin reporting estructurado",
            "Proyectos esporádicos"
          ]
        },
        "personas": {
          "puntuacion": 10,
          "descripcion": "Sin expertise en datos",
          "indicadores": [
            "Sin equipo dedicado",
            "Conocimiento básico en Excel",
            "Sin cultura data-driven"
          ]
        },
        "governance": {
          "puntuacion": 5,
          "descripcion": "Sin gobernanza",
          "indicadores": [
            "Sin políticas de datos",
            "Acceso no controlado",
            "Sin gestión de cambios"
          ]
        }
      },
      "objetivo_madurez": "2- Gestionado",
      "prioridades": [
        "Establecer inventario de datos",
        "Contratar primer analista",
        "Implementar métricas básicas"
      ]
    },
    {
      "id": "ORG-003",
      "nombre": "HealthData Corp",
      "sector": "Salud",
      "tamano": "Grande",
      "nivel_gartner_actual": "3- Definido",
      "nivel_deltha_actual": "Analítico",
      "dimensiones": {
        "datos": {
          "puntuacion": 75,
          "descripcion": "Gestión de datos madura",
          "indicadores": [
            "Catálogo de datos activo",
            "Calidad de datos medida",
            "Lineage implementado"
          ]
        },
        "tecnologia": {
          "puntuacion": 70,
          "descripcion": "Plataforma moderna",
          "indicadores": [
            "Data Lake operativo",
            "ML en producción",
            "Real-time processing"
          ]
        },
        "procesos": {
          "puntuacion": 65,
          "descripcion": "Procesos estandarizados",
          "indicadores": [
            "Metodología definida",
            "Proyectos con ROI",
            "Gestión de modelos"
          ]
        },
        "personas": {
          "puntuacion": 60,
          "descripcion": "Equipo competente",
          "indicadores": [
            "Equipo de 15 personas",
            "Roles especializados",
            "Capacitación continua"
          ]
        },
        "governance": {
          "puntuacion": 55,
          "descripcion": "Gobernanza formal",
          "indicadores": [
            "Comité de datos activo",
            "Políticas documentadas",
            "Auditorías regulares"
          ]
        }
      },
      "objetivo_madurez": "4- Cuantitativo",
      "prioridades": [
        "Implementar observabilidad",
        "Avanzar en MLops",
        "Medir impacto de modelos"
      ]
    },
    {
      "id": "ORG-004",
      "nombre": "Manufacturing Insights Ltd",
      "sector": "Industrial",
      "tamano": "Mediano",
      "nivel_gartner_actual": "4- Cuantitativo",
      "nivel_deltha_actual": "Transformador",
      "dimensiones": {
        "datos": {
          "puntuacion": 85,
          "descripcion": "Excelencia en gestión de datos",
          "indicadores": [
            "Data Mesh implementado",
            "Quality automation",
            "Self-service data"
          ]
        },
        "tecnologia": {
          "puntuacion": 80,
          "descripcion": "Arquitectura avanzada",
          "indicadores": [
            "Cloud-native data platform",
            "MLops enterprise",
            "Real-time ML"
          ]
        },
        "procesos": {
          "puntuacion": 78,
          "descripcion": "Procesos optimizados",
          "indicadores": [
            "CI/CD para datos",
            "A/B testing continuo",
            "Medición de ROI"
          ]
        },
        "personas": {
          "puntuacion": 75,
          "descripcion": "Cultura data-driven",
          "indicadores": [
            "Citizens data scientists",
            "Comunidad activa",
            "Career path definido"
          ]
        },
        "governance": {
          "puntuacion": 72,
          "descripcion": "Gobernanza automatizada",
          "indicadores": [
            "Policy as code",
            "Automated compliance",
            "Stewardship formal"
          ]
        }
      },
      "objetivo_madurez": "5- Optimizado",
      "prioridades": [
        "Innovar con IA generativa",
        "Establecer data marketplace",
        "Liderar ecosistema"
      ]
    },
    {
      "id": "ORG-005",
      "nombre": "BankCorp International",
      "sector": "Financiero",
      "tamano": "Grande",
      "nivel_gartner_actual": "3- Definido",
      "nivel_deltha_actual": "Analítico",
      "dimensiones": {
        "datos": {
          "puntuacion": 70,
          "descripcion": "Datos regulados y controlados",
          "indicadores": [
            "Inventario completo",
            "Calidad auditada",
            "Cumplimiento normativo"
          ]
        },
        "tecnologia": {
          "puntuacion": 68,
          "descripcion": "Infraestructura robusta",
          "indicadores": [
            "Data warehouse enterprise",
            "ETL estructurado",
            "BI corporativo"
          ]
        },
        "procesos": {
          "puntuacion": 60,
          "descripcion": "Procesos en evolución",
          "indicadores": [
            "Metodología de proyectos",
            "Reporting estándar",
            "Gestión de riesgos"
          ]
        },
        "personas": {
          "puntuacion": 55,
          "descripcion": "Equipo en crecimiento",
          "indicadores": [
            "Equipo de 20 personas",
            "Estructura de áreas",
            "Capacitación formal"
          ]
        },
        "governance": {
          "puntuacion": 72,
          "descripcion": "Gobernanza regulatoria",
          "indicadores": [
            "Cumplimiento estricto",
            "Auditorías formales",
            "Políticas robustas"
          ]
        }
      },
      "objetivo_madurez": "4- Cuantitativo",
      "prioridades": [
        "Avanzar en analítica predictiva",
        "Mejorar cultura de datos",
        "Implementar MLops"
      ]
    }
  ],
  "modelo_gartner": {
    "niveles": [
      {
        "nivel": 1,
        "nombre": "Inicial",
        "descripcion": "Procesos reactivos, sin estándarización",
        "caracteristicas": [
          "Sin procesos de datos formalizados",
          "Decisiones basadas en intuición",
          "Sin visibilidad de activos de datos"
        ]
      },
      {
        "nivel": 2,
        "nombre": "Gestionado",
        "descripcion": "Procesos básicos establecidos",
        "caracteristicas": [
          "Procesos de datos reactivos",
          "Gestión básica de calidad",
          "Inventario de datos básico"
        ]
      },
      {
        "nivel": 3,
        "nombre": "Definido",
        "descripcion": "Procesos estándar organizacionalmente",
        "caracteristicas": [
          "Metodología de datos establecida",
          "Data governance formal",
          "Catálogo de datos activo"
        ]
      },
      {
        "nivel": 4,
        "nombre": "Cuantitativo",
        "descripcion": "Gestión optimizada mediante métricas",
        "caracteristicas": [
          "Gestión basada en datos",
          "Métricas de negocio medibles",
          "ML en producción"
        ]
      },
      {
        "nivel": 5,
        "nombre": "Optimizado",
        "descripcion": "Mejora continua e innovación",
        "caracteristicas": [
          "Innovación continua",
          "Data-driven organization",
          "Liderazgo en datos"
        ]
      }
    ]
  },
  "modelo_deltha": {
    "niveles": [
      {
        "nombre": "Novato",
        "descripcion": "Sin capacidades analíticas",
        "enfoque": "Supervivencia"
      },
      {
        "nombre": "Explorador",
        "descripcion": "Analítica básica emergente",
        "enfoque": "Experimentación"
      },
      {
        "nombre": "Analítico",
        "descripcion": "Analítica establecida",
        "enfoque": "Optimización"
      },
      {
        "nombre": "Transformador",
        "descripcion": "Analítica avanzada e innovación",
        "enfoque": "Transformación"
      }
    ]
  }
}

// === ARCHIVO: docs/resumen_comparativo.md ===
# Resumen Comparativo: Modelo de Gartner vs Modelo Deltha

## Introducción

La evaluación de la madurez analítica de una organización constituye un paso fundamental para diseñar estrategias de transformación basadas en datos. Existen múltiples frameworks que permiten diagnosticar el estado actual y planificar la evolución hacia una cultura data-driven. Entre los más reconocidos se encuentran el Modelo de Gartner y el Modelo Deltha, cada uno con un enfoque diferenciado pero complementario.

Este documento presenta un análisis comparativo de ambos modelos, destacando sus dimensiones, niveles y criterios de evaluación. El objetivo es proporcionar una herramienta útil para Arquitectos de Datos y líderes de Analytics que requieren seleccionar el modelo más apropiado según el contexto organizacional.

---

## 1. Modelo de Gartner

### Descripción General

El modelo de madurez analítica de Gartner se centra en la capacidad de la organización para utilizar los datos como activo estratégico. Evalúa la transición desde una postura reactiva hacia una cultura proactiva donde los datos guían la toma de decisiones en todos los niveles jerárquicos.

### Niveles de Madurez Gartner

| Nivel | Denominación | Descripción |
|-------|--------------|-------------|
| 1 | **Ansible / Awareness** | La organización carece de infraestructura y competencias en analytics. Las decisiones se toman por intuición y experiencia. No existe una estrategia de datos formalizada. |
| 2 | **Exploring** | Primeros proyectos piloto aislados. Se comienza a reconocer el valor de los datos, pero no hay gobernanza ni estándares definidos. Las iniciativas surgen de forma descentralizada. |
| 3 | **Foundational** | Se establecen las bases tecnológicas y organizacionales. Se implementan data warehouses, se define una gobernanza básica y se contratan los primeros perfiles especializados en datos. |
| 4 | **Operational** | Los análisis están integrados en los procesos operativos diarios. Existe un equipo de datos estructurado, herramientas de BI desplegadas y procesos de reporting automatizados. |
| 5 | **Analytical Enterprise** | La organización es genuinamente data-driven. Los datos son fuente de ventaja competitiva. Se utiliza analítica avanzada, ML e IA de forma sistemática. La cultura de datos permea todos los niveles. |

### Dimensiones de Evaluación Gartner

- **Infraestructura tecnológica**: Capacidad de almacenamiento, procesamiento y disponibilidad de datos.
- **Talento y competencias**: Perfiles técnicos, capacitación en analytics, cultura de datos.
- **Gobernanza**: Políticas de calidad, seguridad, privacidad y gestión de datos.
- **Procesos de decisión**: Grado de integración de insights en la toma de decisiones.
- **Estrategia de datos**: Existencia de un plan director de datos alineado con el negocio.

---

## 2. Modelo Deltha

### Descripción General

El modelo Deltha, desarrollado por Stefan Van Dongen y colaboradores, se enfoca en la evolución de las capacidades analíticas desde el reporting básico hasta la optimización predictiva. Es particularmente útil para organizaciones que buscan evolucionar gradualmente sus competencias técnicas.

### Niveles de Madurez Deltha

| Nivel | Denominación | Descripción |
|-------|--------------|-------------|
| 1 | **Reporting** | Generación de reportes estáticos y dashboards básicos. Los datos se extraen manualmente y se presentan en formato tabular. No hay automatización ni análisis profundo. |
| 2 | **Analysis** | Análisis ad-hoc y exploratorio. Se utilizan herramientas de BI interactivas. Los usuarios pueden explorar datos y generar Visualizaciones sin depender de TI. |
| 3 | **Predictive** | Se implementan modelos estadísticos y de machine learning. La organización comienza a anticipar tendencias y comportamientos. Se formalizan procesos de modelado. |
| 4 | **Optimization** | Los modelos predictivos se integran en procesos operativos para automatizar decisiones. Se utiliza analítica prescriptiva para optimizar procesos. |
| 5 | **Data-Driven** | La organización opera en tiempo real con datos. Las decisiones se toman de forma automatizada basada en modelos. Existe una cultura de experimentación y mejora continua. |

### Dimensiones de Evaluación Deltha

- **Capacidad técnica**: Herramientas, infraestructura y automatización del pipeline de datos.
- **Habilidades analíticas**: Competencia en estadística, modelado y visualización.
- **Integración operativa**: Grado en que los insights se traducen en acciones automatizadas.
- **Cultura de datos**: Democratización del acceso y uso de datos en la organización.
- **Impacto de negocio**: Contribución medible de los análisis a los resultados organizacionales.

---

## 3. Análisis Comparativo

### Similitudes Fundamentales

Ambos modelos comparten una estructura de cinco niveles progresivos que reflejan la evolución natural de una organización hacia la excelencia analítica. Los niveles superiores de ambos modelos convergen en el concepto de "organización data-driven", donde los datos son parte integral de la cultura y estrategia empresarial.

Ambos frameworks reconocen la importancia de:

- La infraestructura tecnológica como habilitador
- El talento y las competencias especializadas
- La gobernanza y calidad de datos
- La integración de insights en la toma de decisiones
- La evolución gradual como requisito para el éxito

### Diferencias Clave

| Aspecto | Modelo Gartner | Modelo Deltha |
|---------|----------------|---------------|
| **Enfoque principal** | Transformación cultural y estratégica | Evolución de capacidades técnicas |
| **Unidad de análisis** | Organización completa | Procesos y capacidades analíticas |
| **Nivel inicial** | Ausencia total de conciencia analítica | Reporting básico existente |
| **Nivel final** | Ventaja competitiva basada en datos | Optimización en tiempo real |
| **Énfasis** | Estrategia y gobernanza | Técnicas y automatización |
| **Aplicabilidad** | Organizaciones en cualquier estado | Organizaciones con al menos reporting |

### Selección del Modelo Apropiado

La elección entre ambos modelos depende del contexto organizacional:

- **Gartner** resulta más adecuado para organizaciones que inician su viaje de transformación de datos y requieren un enfoque holístico que abarque estrategia, cultura y tecnología.

- **Deltha** es preferible para organizaciones que ya tienen madurez en reporting y buscan evolucionar hacia capacidades analíticas avanzadas y automatización.

En la práctica, muchos profesionales utilizan ambos modelos de forma complementaria: Gartner para el diagnóstico estratégico de alto nivel y Deltha para planificar la evolución técnica específica.

---

## 4. Conclusiones

La evaluación de la madurez analítica no es un ejercicio puntual sino un proceso continuo que permite a las organizaciones identificar brechas y priorizar inversiones. El conocimiento profundo de los modelos disponibles permite seleccionar el framework más apropiado o combinarlos para obtener una visión integral del estado actual y el camino hacia la excelencia analítica.

La transformación hacia una organización data-driven requiere compromiso del liderazgo, inversión sostenida en tecnología y talento, y una gestión del cambio efectiva. Los modelos de madurez proporcionan el mapa; la ejecución depende de la voluntad organizacional.

---

*Documento generado como parte del proyecto de Evaluación de Madurez Analítica.*
*Versión: 1.0* // === ARCHIVO: docs/informe_evaluacion.md ===
# Informe de Evaluación de la Madurez Analítica Actual

## 1. Contexto y Alcance

El presente informe documenta los resultados de la evaluación de madurez analítica aplicada a una organización del sector financiero. La evaluación se realizó utilizando los frameworks de Gartner y Deltha, proporcionando una visión integral del estado actual de las capacidades analíticas de la empresa.

El alcance incluye la revisión de infraestructura tecnológica, procesos de datos, talento humano, gobernanza y grado de integración de insights en la toma de decisiones. Los hallazgos se basan en entrevistas con stakeholders clave, revisión de documentación existente y análisis de los sistemas de información en producción.

---

## 2. Resumen Ejecutivo

La organización evaluada se encuentra actualmente en un estado de madurez analítica **intermedio-bajo**, situándose en el **Nivel 2 (Exploring)** según el modelo Gartner y en el **Nivel 2 (Analysis)** según el modelo Deltha.

**Hallazgos principales:**

- Existe conciencia creciente sobre el valor de los datos, pero no hay una estrategia de datos formalizada.
- Los proyectos de analytics son aislados y no están coordinados centralmente.
- La infraestructura de datos es fragmentada, con múltiples fuentes no integradas.
- El talento técnico especializado es limitado y no hay un equipo de datos estructurado.
- La gobernanza de datos es incipiente, con riesgos identificados en calidad y seguridad.
- Los procesos de toma de decisiones dependen principalmente de la experiencia y criterio humano.

**Puntuación agregada:** 2.3 / 5.0 (Escala Gartner)

---

## 3. Detalle de la Evaluación por Dimensión

### 3.1 Infraestructura Tecnológica

**Estado actual:**

La organización cuenta con sistemas transaccionales legacy que almacenan datos en bases de datos relacionales heterogéneas. No existe un data warehouse centralizado; los reportes se generan directamente desde los sistemas operativos mediante consultas SQL manuales.

Las herramientas de business intelligence son limitadas: se utiliza Microsoft Excel como herramienta principal de análisis y visualización, con algunos dashboards básicos en Power BI que no están integrados con las fuentes de datos en tiempo real.

**Hallazgos específicos:**

- Más de 15 sistemas fuente diferentes sin integración automatizada
- Ausencia de un data lake o data warehouse moderno
- Procesos de ETL inexistentes; la extracción de datos es manual y propensa a errores
- Backups de datos inconsistentes entre sistemas
- Latencia de datos: la información tiene entre 24 y 72 horas de antigüedad

**Nivel Gartner:** 2 / 5
**Nivel Deltha:** 1 / 5

### 3.2 Talento y Competencias

**Estado actual:**

El equipo de TI está compuesto por 8 profesionales especializados en infraestructura y soporte. No existe un equipo dedicado a análisis de datos. Las competencias en analytics se limitan a usuarios de negocio que utilizan Excel de forma avanzada.

No se han contratado perfiles de científico de datos, ingeniero de datos o arquitecto de datos. La organización carece de un Chief Data Officer (CDO) o equivalente.

**Hallazgos específicos:**

- Cero perfiles de científico de datos
- Dos analistas de negocio con conocimientos básicos de SQL y Excel
- No hay programas de capacitación en analytics
- Dependencia excesiva de un grupo reducido de personas para tareas críticas de datos
- Ausencia de certificaciones en herramientas de analytics

**Nivel Gartner:** 2 / 5
**Nivel Deltha:** 2 / 5

### 3.3 Gobernanza de Datos

**Estado actual:**

No existe un marco de gobernanza de datos formalizado. No hay políticas documentadas de calidad de datos, seguridad, privacidad o gestión del ciclo de vida de la información. La responsabilidad sobre los datos está dispersa entre los propietarios de los sistemas.

**Hallazgos específicos:**

- Ausencia de un catálogo de datos empresarial
- No se realizan controles de calidad de datos de forma sistemática
- Políticas de seguridad inconsistentes entre sistemas
- No hay un inventario de datos sensibles ni controles de privacidad implementados
- Dificultad para rastrear el origen (lineage) de los datos

**Nivel Gartner:** 1 / 5
**Nivel Deltha:** 2 / 5

### 3.4 Procesos de Decisión

**Estado actual:**

Las decisiones estratégicas se toman principalmente basadas en la experiencia del equipo directivo y reportes financieros trimestrales. No existe una cultura de toma de decisiones basada en evidencia; los datos se utilizan principalmente para cumplimiento regulatorio y reporting obligatorio.

**Hallazgos específicos:**

- Las decisiones operativas diarias no utilizan analytics
- No hay procesos de negocio que dependan de modelos predictivos
- Los reportes se generan con fines de cumplimiento, no de insight
- Baja demanda de análisis por parte de los usuarios de negocio
- No existen experimentos A/B ni metodologías de testing

**Nivel Gartner:** 2 / 5
**Nivel Deltha:** 1 / 5

### 3.5 Estrategia de Datos

**Estado actual:**

No existe un plan director de datos ni una estrategia formalizada de analytics. Las iniciativas de datos surgen de forma reactiva, respondiendo a problemas específicos o requerimientos regulatorios, sin una visión de largo plazo.

**Hallazgos específicos:**

- No hay un documento de estrategia de datos aprobado por la dirección
- Ausencia de métricas de éxito para iniciativas de datos
- No existen roadmap de capacidades de datos
- La inversión en datos es reactiva y no planificada
- No hay alineación entre estrategia de TI y estrategia de datos

**Nivel Gartner:** 1 / 5
**Nivel Deltha:** N/A

---

## 4. Matriz de Madurez Consolidada

| Dimensión | Gartner | Deltha |
|-----------|---------|--------|
| Infraestructura | 2 | 1 |
| Talento | 2 | 2 |
| Gobernanza | 1 | 2 |
| Decisiones | 2 | 1 |
| Estrategia | 1 | N/A |
| **Promedio** | **1.6** | **1.5** |

---

## 5. Análisis de Brechas

### Brecha Crítica: Estrategia y Gobernanza

La ausencia de una estrategia de datos formalizada y un marco de gobernanza constituye el principal impedimento para la evolución de la madurez analítica. Sin estos fundamentos, cualquier inversión en tecnología o talento no producirá el retorno esperado.

### Brecha Significativa: Infraestructura de Datos

La fragmentación de sistemas y la ausencia de integración impide la generación de insights holísticos. Los datos operan en silos, limitando la capacidad de análisis cross-funcional.

### Brecha Significativa: Talento Especializado

La organización carece de los perfiles necesarios para liderar la transformación analítica. La dependencia de consultores externos no es sostenible y no genera capacidad interna.

---

## 6. Recomendaciones de Priorización

Considerando el estado actual y las brechas identificadas, se recomienda el siguiente orden de prioridad:

1. **Corto plazo (0-6 meses):** Establecer gobernanza básica y designar responsables de datos
2. **Mediano plazo (6-18 meses):** Desarrollar estrategia de datos y contratar talento clave
3. **Largo plazo (18-36 meses):** Implementar infraestructura moderna y escalar capacidades

---

## 7. Conclusiones

La organización tiene una oportunidad significativa de transformar su operación mediante el uso estratégico de datos. Sin embargo, el camino hacia la excelencia analítica requiere inversiones sostenidas en tecnología, talento y cambio cultural.

El diagnóstico actual refleja una organización que reconoce el valor de los datos pero carece de los fundamentos necesarios para materializar ese valor. La evolución hacia niveles superiores de madurez es factible siempre que exista compromiso del liderazgo y una planificación rigurosa.

---

*Informe preparado por el Equipo de Arquitectura de Datos*
*Fecha de elaboración: 2024*
*Clasificación: Confidencial - Uso Interno* // === ARCHIVO: docs/recomendaciones.md ===
# Recomendaciones para Mejorar la Madurez Analítica

## 1. Resumen de la Situación Actual

Tras la evaluación de madurez analítica realizada según los modelos Gartner y Deltha, la organización se encuentra en el Nivel 2 (Exploring) y Nivel 2 (Analysis) respectivamente. Este diagnóstico indica que la empresa ha superado la fase de ignorancia total sobre el valor de los datos, pero aún no ha establecido las bases necesarias para escalar sus capacidades analíticas.

Las brechas más críticas identificadas son la ausencia de estrategia de datos, la fragmentación de la infraestructura tecnológica, la falta de talento especializado y la inexistencia de un marco de gobernanza. El presente documento detalla las recomendaciones específicas para abordar cada una de estas brechas y progresar hacia niveles superiores de madurez.

---

## 2. Recomendaciones Estratégicas

### 2.1 Establecer una Estrategia de Datos Formalizada

**Objetivo:** Definir una visión clara y un plan de acción para la transformación analítica.

**Acciones recomendadas:**

- Contratar o designar un Chief Data Officer (CDO) con autoridad y presupuesto propio
- Desarrollar un documento de estrategia de datos alineado con los objetivos estratégicos del negocio
- Definir métricas de éxito y KPIs para iniciativas de datos
- Establecer un governance board de datos con representantes de todas las áreas
- Crear un roadmap de capacidades de datos a 3 años con hitos medibles

**Impacto esperado:** Alineación de esfuerzos, priorización de inversiones, reducción de iniciativas aisladas.

**Prioridad:** Crítica

### 2.2 Implementar un Marco de Gobernanza de Datos

**Objetivo:** Asegurar la calidad, seguridad y uso apropiado de los datos.

**Acciones recomendadas:**

- Definir políticas de calidad de datos (completitud, consistencia, oportunidad, precisión)
- Establecer un catálogo de datos empresariales que documente activos de datos clave
- Implementar procesos de gestión de datos maestros y metadatos
- Crear políticas de seguridad y privacidad alineadas con regulaciones aplicables
- Definir roles y responsabilidades de datos (data owners, data stewards, data custodians)
- Implementar un proceso de gestión de incidentes de calidad de datos

**Impacto esperado:** Confianza en los datos, reducción de errores, cumplimiento regulatorio.

**Prioridad:** Crítica

---

## 3. Recomendaciones de Infraestructura

### 3.1 Construir una Plataforma de Datos Centralizada

**Objetivo:** Integrar las múltiples fuentes de datos en una plataforma unificada que permita análisis holísticos.

**Acciones recomendadas:**

- Implementar un data warehouse moderno (Snowflake, BigQuery o Databricks)
- Establecer un data lake para almacenar datos crudos y no estructurados
- Desarrollar pipelines de datos automatizados (ETL/ELT) desde las fuentes
- Implementar un modelo de datos corporativo (data model empresarial)
- Configurar procesos de ingestión en tiempo real para datos críticos
- Implementar herramientas de observabilidad de datos

**Impacto esperado:** Acceso unificado a datos, reducción de silos, capacidad de análisis avanzado.

**Prioridad:** Alta

### 3.2 Modernizar las Herramientas de Analytics

**Objetivo:** Dotar a los usuarios de herramientas adecuadas para el análisis y visualización.

**Acciones recomendadas:**

- Implementar una plataforma de BI moderna (Power BI, Tableau o Looker)
- Capacitar a usuarios de negocio en el uso de herramientas de autoservicio
- Desplegar notebooks Jupyter para análisis exploratorio
- Evaluar herramientas de machine learning para análisis predictivo
- Implementar dashboards operativos en tiempo real

**Impacto esperado:** Democratización del acceso a insights, mayor velocidad de análisis.

**Prioridad:** Alta

---

## 4. Recomendaciones de Talento

### 4.1 Construir un Equipo de Datos Especializado

**Objetivo:** Contar con el talento necesario para ejecutar la estrategia de datos.

**Acciones recomendadas:**

- Contratar un equipo inicial mínimo: 1 data engineer, 1 data analyst, 1 ML engineer
- Definir карьерные path para profesionales de datos dentro de la organización
- Establecer alianzas con universidades y bootcamps para reclutamiento
- Implementar un programa de retención de talento técnico
- Desarrollar competencias internas mediante mentorship y rotación de roles

**Impacto esperado:** Capacidad técnica para ejecutar iniciativas, reducción de dependencia externa.

**Prioridad:** Alta

### 4.2 Desarrollar Capacidades de Analytics en Negocio

**Objetivo:** Crear una cultura de datos en toda la organización.

**Acciones recomendadas:**

- Lanzar un programa de alfabetización en datos para todos los empleados
- Capacitar a usuarios de negocio en herramientas de BI de autoservicio
- Crear comunidades de práctica de analytics entre áreas
- Establecer programas de certificación interna en analytics
- Fomentar el uso de datos en la toma de decisiones mediante casos de éxito

**Impacto esperado:** Cultura data-driven, demanda de analytics, adopción tecnológica.

**Prioridad:** Media

---

## 5. Recomendaciones de Procesos

### 5.1 Integrar Analytics en Procesos de Negocio

**Objetivo:** Convertir los insights en acciones que generen valor medible.

**Acciones recomendadas:**

- Identificar procesos de negocio con mayor potencial de impacto analítico
- Implementar modelos predictivos para Scoring de clientes, detección de fraude, predicción de churn
- Automatizar decisiones operativas basadas en reglas derivadas de análisis
- Establecer procesos de experimentación (A/B testing) para iniciativas de mejora
- Crear ciclos de retroalimentación entre modelos y resultados de negocio

**Impacto esperado:** ROI demostrable de analytics, optimización de procesos, ventaja competitiva.

**Prioridad:** Media

### 5.2 Establecer Métricas y Medición de Impacto

**Objetivo:** Demostrar el valor de las inversiones en datos.

**Acciones recomendadas:**

- Definir un framework de métricas para evaluar el éxito de iniciativas de datos
- Implementar un dashboard de monitoreo de KPIs de datos
- Realizar análisis de ROI de proyectos de analytics
- Publicar informes periódicos de valor generado por datos
- Vincular compensación de equipo de datos con métricas de impacto

**Impacto esperado:** Justificación de inversiones, mejora continua, accountability.

**Prioridad:** Media

---

## 6. Roadmap de Implementación Sugerido

### Fase 1: Fundamentos (Meses 1-6)

| Iniciativa | Entregable |
|------------|-------------|
| Designación de CDO | CDO nombrado y equipo directivo |
| Estrategia de datos | Documento de estrategia aprobado |
| Gobernanza básica | Políticas de calidad y seguridad documentadas |
| Equipo inicial | 3 profesionales de datos contratados |

### Fase 2: Plataforma (Meses 7-18)

| Iniciativa | Entregable |
|------------|-------------|
| Data warehouse | Plataforma en producción |
| Pipelines de datos | 80% de fuentes integradas |
| Catálogo de datos | Activos críticos documentados |
| BI moderna | Herramientas desplegadas y capacitadas |

### Fase 3: Escalamiento (Meses 19-36)

| Iniciativa | Entregable |
|------------|-------------|
| Modelos predictivos | 5+ modelos en producción |
| Automatización | Procesos optimizados con ML |
| Analytics en tiempo real | Dashboards operativos |
| Excelencia operativa | Maturity nivel 4 Gartner |

---

## 7. Consideraciones de Riesgo

### Riesgo 1: Resistencia al Cambio

La transformación analítica requiere cambios culturales significativos. La organización debe preparar al personal para adoptar nuevas formas de trabajar basadas en datos.

**Mitigación:** Comunicación efectiva, casos de éxito tempranos, involucramiento de líderes.

### Riesgo 2: Sobrecarga de Iniciativas

Intentar implementar demasiadas cosas simultáneamente puede diluir recursos y generar fatiga.

**Mitigación:** Priorización rigurosa, enfoque en iniciativas de alto impacto, entregables incrementales.

### Riesgo 3: Dependencia de Proveedores

La dependencia excesiva de vendors tecnológicos puede limitar la flexibilidad futura.

**Mitigación:** Arquitectura abierta, evitar lock-in, mantener competencias internas.

---

## 8. Conclusiones

La organización tiene ante sí una oportunidad transformadora. La evolución hacia niveles superiores de madurez analítica no es solo una cuestión tecnológica sino un cambio cultural y organizacional que requiere liderazgo compromiso y persistencia.

Las recomendaciones presentadas proporcionan un camino claro pero exigente. El éxito dependerá de la capacidad para ejecutar de forma disciplinada, medir resultados y ajustar el curso según los aprendizajes.

La inversión en capacidades analíticas no es un gasto sino una inversión estratégica que posicionará a la organización para competir efectivamente en un entorno cada vez más basado en datos.

---

*Documento preparado por el Equipo de Arquitectura de Datos*
*Para consultas sobre este informe, contactar al responsable del proyecto de evaluación de madurez.*


// === ARCHIVO: tests/test_evaluacion.py ===
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
// === ARCHIVO: tests/test_recomendaciones.py ===
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

```
