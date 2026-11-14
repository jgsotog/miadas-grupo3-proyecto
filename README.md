# Proyecto Integrador - Grupo 3

**Programa:** Maestría en Inteligencia Artificial y Data Science para la Transformación de Negocios (MIADAS)  
**Institución:** Universidad Mayor de San Andrés (UMSA) – Postgrado en Informática  
**Módulo:** Módulo 2: Preparación, Recopilación y Análisis Exploratorio de Datos  
**Docente:** M.Sc. Marcelo Pinto Macedo  
**Equipo:** Grupo 3  
**Integrantes:** María Huampo, Limbert Nelson Escobar Mamani, Cristian Kelvin Espinoza Ortega, Jaime Gabriel Soto Gonzales  
**Caso de Estudio:** Análisis de Ingreso Laboral y Gastos de los Hogares en Bolivia (Encuesta de Hogares EH2025 · INE)

---

## 📌 Pregunta Central de Negocio

> **¿En qué medida la brecha de ingreso laboral entre el área urbana y rural condiciona la estructura del gasto (alimentos vs. no alimentos) en los nueve departamentos de Bolivia, y cuáles departamentos registran mayor vulnerabilidad presupuestaria?**

### Estructura y Marco Analítico del Cuaderno
1. **Sesión 1 (S1) · Tipos de datos y escalas de medición:**
   - Taxonomía de escalas de medición (Stevens, 1946).
   - Tipificación de variables cualitativas y cuantitativas.
   - Tratamiento de fechas (`datetime64`) y diagnóstico de sesgos de distribución.
2. **Sesión 2 (S2) · Recopilación de datos y diseño muestral:**
   - Modelado del tamaño muestral probabilístico (fórmula de Cochran, 1977).
   - Simulación de representatividad territorial.
   - Justificación del muestreo estratificado multietápico y ponderación con factores de expansión (`factor`).
3. **Sesión 3 (S3) · Fuentes, extracción e integración relacional:**
   - Arquitectura relacional multinivel (clave primaria/foránea: `folio`).
   - Pipeline de agregación de persona a hogar.
   - Resolución cuantitativa: Brecha de ingreso laboral, cumplimiento de la Ley de Engel y tasas de déficit presupuestario por departamento y área.
4. **Cierre Metodológico:**
   - Ficha técnica e informe de calidad de datos bajo el marco CRISP-DM (fase 2).

---

## 🐍 Requisitos de Entorno y Versión de Python

- **Versión de Python utilizada en el desarrollo:** `Python 3.13` (compatible con `Python >= 3.10`).
- **Librerías principales:**
  - `pandas`: Manipulación y análisis tabular de microdatos.
  - `numpy`: Cálculos numéricos y transformaciones condicionales vectorizadas.
  - `matplotlib` & `seaborn`: Visualización estadística de datos.
  - `pyreadstat`: Lectura y conversión de archivos de microdatos SPSS (`.sav`).
  - `ipykernel`: Ejecución interactiva de Jupyter Notebooks.
  - `openpyxl`: Soporte para lectura y escritura de hojas Excel.

---

## 🚀 Configuración del Entorno Virtual Local

### 1. Clonar o abrir la carpeta del repositorio
Abre una terminal (PowerShell o Git Bash) en la raíz del proyecto.

### 2. Crear el entorno virtual
Ejecuta el siguiente comando para crear un entorno virtual aislado (nombrado `.venv`):
```powershell
python -m venv .venv
```

### 3. Activar el entorno virtual
- **En Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  *(Si PowerShell restringe la ejecución de scripts, habilítala con: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`)*
- **En Windows (CMD):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```
- **En macOS / Linux (Bash/Zsh):**
  ```bash
  source .venv/bin/activate
  ```

### 4. Instalar las dependencias
Con el entorno virtual activado, instala todas las librerías necesarias ejecutando:
```powershell
pip install -r requirements.txt
```

---

## 💻 Uso desde Visual Studio Code (VS Code)

1. **Abrir la carpeta del proyecto en VS Code:**
   Abre la carpeta raíz `miadas-grupo3-proyecto` en VS Code.

2. **Seleccionar el intérprete de Python:**
   - Presiona `Ctrl + Shift + P` (o `Cmd + Shift + P` en macOS).
   - Escribe y selecciona: `Python: Select Interpreter`.
   - Elige el entorno virtual que acabas de crear: `Python (.venv) .\.venv\Scripts\python.exe`.

3. **Ejecutar el Jupyter Notebook (`miadas-grupo3-proyecto.ipynb`):**
   - Abre el archivo `miadas-grupo3-proyecto.ipynb`.
   - En la esquina superior derecha del editor del notebook, haz clic en **"Select Kernel"** (o "Elegir Kernel").
   - Selecciona **Python Environments...** y haz clic en `.venv (Python 3.13.x)`.
   - Ya puedes ejecutar celda por celda o presionar **"Run All"** (Ejecutar todo).

4. **Ejecutar el conversor SPSS a CSV (`convertir_sav.py`):**
   - Si cuentas con los archivos `.sav` originales del INE, puedes convertirlos automáticamente a `.csv` ejecutando:
   ```powershell
   python convertir_sav.py
   ```

---

## ☁️ Cómo Importar y Ejecutar en Google Colab

Puedes ejecutar el proyecto directamente en la nube de Google Colab siguiendo estos sencillos pasos:

### Opción 1: Abrir directamente desde Google Colab
1. Ve a [Google Colab](https://colab.research.google.com/).
2. En la ventana de bienvenida:
   - **Desde GitHub:** Selecciona la pestaña **GitHub**, pega el enlace de este repositorio y selecciona el cuaderno `miadas-grupo3-proyecto.ipynb`.
   - **Subiendo el archivo:** Selecciona la pestaña **Upload** (Subir) y arrastra el archivo local `miadas-grupo3-proyecto.ipynb`.

### Opción 2: Subir los datos a Colab
Debido a que los archivos `.csv` y `.sav` están excluidos del repositorio por su peso (ver sección de `.gitignore`), debes cargar los datos en tu entorno de Colab de una de las siguientes formas:

#### Forma A · Subida directa a la sesión (Archivos temporales)
1. En el panel lateral izquierdo de Colab, haz clic en el ícono de carpeta 📁 (**Archivos**).
2. Haz clic en el ícono de **Subir al almacenamiento de sesión** y sube los 4 archivos CSV:
   - `EH2025_Vivienda_1.csv`
   - `EH2025_Persona.csv`
   - `EH2025_Gastos_No_Alimentarios.csv`
   - `EH2025_Gastos_Alimentarios.csv`
3. Ejecuta las celdas del cuaderno normalmente.

#### Forma B · Conectar Google Drive (Recomendada para archivos pesados)
1. Sube los archivos `.csv` a una carpeta de tu Google Drive (por ejemplo, `MiDrive/Colab_Data/`).
2. En la primera celda de tu cuaderno en Colab, monta tu Google Drive:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Modifica la ruta de lectura de los CSV en la celda 2 para apuntar a tu carpeta de Drive:
   ```python
   DATA_PATH = '/content/drive/MyDrive/Colab_Data/'
   vivienda = pd.read_csv(DATA_PATH + 'EH2025_Vivienda_1.csv', low_memory=False)
   persona = pd.read_csv(DATA_PATH + 'EH2025_Persona.csv', low_memory=False)
   gastos_no_alim = pd.read_csv(DATA_PATH + 'EH2025_Gastos_No_Alimentarios.csv', low_memory=False)
   gastos_alim = pd.read_csv(DATA_PATH + 'EH2025_Gastos_Alimentarios.csv', usecols=['folio', 'depto', 'area', 'producto', 's08a_04', 's08a_07'])
   ```

*(Nota: En Colab las librerías `pandas`, `numpy` y `matplotlib` ya vienen preinstaladas. Si requieres convertir archivos `.sav` en Colab, simplemente instala `pyreadstat` con `!pip install pyreadstat`).*

---

## 📁 Archivos del Proyecto y Gestión con Git

El archivo `.gitignore` ha sido configurado para excluir:
- **Entornos virtuales:** `.venv/`, `venv/`, etc., para evitar subir paquetes binarios y dependencias locales.
- **Bases de datos y microdatos:** `*.sav` y `*.csv`, para respetar el límite de tamaño de Git/GitHub (varios de estos archivos superan los 80 MB) y seguir las directrices de integridad de repositorios.
- **Caché y temporales:** `__pycache__/`, `.ipynb_checkpoints/`, etc.

### Archivos incluidos en el repositorio:
- `miadas-grupo3-proyecto.ipynb`: Cuaderno Jupyter con todo el flujo de análisis, agregación y visualización.
- `convertir_sav.py`: Script de Python para procesar y transformar microdatos `.sav` a formato `.csv`.
- `Diccionario_datos.pdf` y `Diccionario_datos.xml`: Metadatos y codificación oficial de la Encuesta de Hogares (INE).
- `requirements.txt`: Lista de dependencias del proyecto con versiones fijadas.
- `.gitignore`: Reglas de exclusión de Git.
- `README.md`: Documentación técnica y guía de ejecución del proyecto.
