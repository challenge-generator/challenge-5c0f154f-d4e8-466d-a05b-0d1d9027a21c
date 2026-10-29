# Evaluación de Madurez Analítica en una Organización Dirigida por Datos

Como Arquitecto de Datos en una organización financiera, debes evaluar la madurez analítica de la empresa utilizando el Modelo de Gartner y el Modelo Deltha. Identifica las características de una organización dirigida por datos y determina en qué nivel de madurez se encuentra actualmente la empresa.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Assessment |
| **Nivel** | senior-l2 |
| **Tipo** | theoretical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Exploración de Modelos de Madurez Analítica

**Objetivo:** Comprender y comparar los Modelos de Gartner y Deltha para evaluar la madurez analítica.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Investiga y describe los Modelos de Gartner y Deltha.
- Identifica las principales diferencias y similitudes entre ambos modelos.

**Entregable:** Resumen comparativo de los Modelos de Gartner y Deltha.

<details>
<summary>Pistas de conocimiento</summary>

- Características de una organización dirigida por datos.
- Niveles de madurez analítica según ambos modelos.

</details>

### Fase 2: Evaluación de la Madurez Analítica Actual

**Objetivo:** Aplicar los modelos para evaluar la madurez analítica actual de la organización.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Utiliza los Modelos de Gartner y Deltha para evaluar el nivel de madurez analítica de la organización.
- Identifica las áreas de mejora y los desafíos actuales.

**Entregable:** Informe de evaluación de la madurez analítica actual de la organización.

<details>
<summary>Pistas de conocimiento</summary>

- Criterios de evaluación según cada modelo.
- Ejemplos de áreas de mejora en la madurez analítica.

</details>

### Fase 3: Recomendaciones para Mejorar la Madurez Analítica

**Objetivo:** Proponer recomendaciones para avanzar en la madurez analítica de la organización.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Basándote en la evaluación realizada, propone recomendaciones para mejorar la madurez analítica.
- Considera los trade-offs y las implicaciones de cada recomendación.

**Entregable:** Documento de recomendaciones para mejorar la madurez analítica de la organización.

<details>
<summary>Pistas de conocimiento</summary>

- Estrategias para avanzar en la madurez analítica.
- Trade-offs entre diferentes niveles de madurez.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué son los Modelos de Gartner y Deltha y cómo se utilizan para evaluar la madurez analítica?
- **paraQueSirve**: ¿Para qué sirve evaluar la madurez analítica de una organización?
- **comoSeUsa**: ¿Cómo se aplican los Modelos de Gartner y Deltha para evaluar la madurez analítica actual de una organización?
- **erroresComunes**: ¿Cuáles son los errores comunes al evaluar la madurez analítica?
- **queDecisionesImplica**: ¿Qué decisiones implica proponer recomendaciones para mejorar la madurez analítica?

## Criterios de Evaluacion

- Comprensión y comparación de los Modelos de Gartner y Deltha.
- Evaluación precisa de la madurez analítica actual de la organización.
- Propuesta de recomendaciones efectivas para mejorar la madurez analítica.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && pytest -q
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
