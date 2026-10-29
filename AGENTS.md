# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Evaluación de Madurez Analítica en una Organización Dirigida por Datos**.

| | |
|---|---|
| Tema | Assessment |
| Nivel | senior-l2 |
| Chapter | Ciencia de Datos — Científico |
| Especialidad | Cientifico de datos |
| Stack | Python 3.13 / Jupyter Notebook + MLflow |
| Patron arquitectonico | Pipeline analítico con capas de exploración, evaluación y recomendaciones |
| Tiempo estimado | 8 horas |

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `notebooks/eda.ipynb con el analisis exploratorio`
- `src/data con la carga y el preprocesamiento`
- `src/features con la ingenieria de variables`
- `src/models con entrenamiento y evaluacion`
- `src/serve con la exposicion del modelo (inferencia)`
- `tests/ con validacion de metricas esperadas`

Dependencias:

- python 3.13
- jupyter n/a
- pandas n/a
- numpy n/a
- matplotlib n/a
- scikit-learn n/a
- pytest n/a
- mlflow n/a

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && pytest -q` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && pytest -q` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Exploración de Modelos de Madurez Analítica**: Resumen comparativo de los Modelos de Gartner y Deltha.
- **Fase 2 — Evaluación de la Madurez Analítica Actual**: Informe de evaluación de la madurez analítica actual de la organización.
- **Fase 3 — Recomendaciones para Mejorar la Madurez Analítica**: Documento de recomendaciones para mejorar la madurez analítica de la organización.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Lo que falta y tenes que completar

### 1. Archivos que la arquitectura declara (4 de 11)

La propuesta arquitectonica del reto los lista y no llegaron al repo. Crealos con implementacion real, respetando la capa en la que viven:

- [ ] `notebooks/analisis_exploratorio_modelos.ipynb`
- [ ] `notebooks/evaluacion_madurez_actual.ipynb`
- [ ] `docs/informe_evaluacion.md`
- [ ] `docs/recomendaciones.md`

### Presentes (7)

- `pyproject.toml`
- `src/evaluation/madurez_analitica.py`
- `src/recommendations/recomendaciones.py`
- `data/madurez_ejemplo.json`
- `docs/resumen_comparativo.md`
- `tests/test_evaluacion.py`
- `tests/test_recomendaciones.py`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `notebooks`
- `data`
- `src`
- `src/evaluation`
- `src/recommendations`
- `docs`
- `tests`

## Verificacion

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **Pipeline analítico con capas de exploración, evaluación y recomendaciones**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Ciencia de Datos, Especialidad Arquitecto de Datos, Senior
- Brecha que el reto ataca: Conoce y experimenta los niveles de madurez de analítica (Modelo de Gartner, Modelo Deltha), características de una organización dirigida por datos. Brecha de conocimiento en evaluación de madurez analítica
- Mision: Candidato con experiencia como Arquitecto de Datos.

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
