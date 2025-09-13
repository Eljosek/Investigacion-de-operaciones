# Guía de Despliegue - Programación Lineal Web

Esta aplicación puede desplegarse en varias plataformas gratuitas. A continuación se muestran las opciones más recomendadas:

## 🚀 Opción 1: Render (RECOMENDADO)

Render es una plataforma gratuita que permite desplegar aplicaciones Flask fácilmente.

### Pasos para desplegar en Render:

1. **Sube tu código a GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/tu-usuario/programacion-lineal-web.git
   git push -u origin main
   ```

2. **Ve a [render.com](https://render.com) y crea una cuenta**

3. **Crea un nuevo Web Service:**
   - Conecta tu repositorio de GitHub
   - Configura los siguientes campos:
     - **Name:** `programacion-lineal-web`
     - **Environment:** `Python 3`
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `python app.py`

4. **Configura las variables de entorno:**
   - `PYTHON_VERSION`: `3.13.7`
   - `PORT`: `5000`

5. **Despliega y obtén tu URL pública**

### URL de ejemplo:
`https://programacion-lineal-web.onrender.com`

## 🌐 Opción 2: Heroku

### Archivos necesarios para Heroku:

#### Procfile
```
web: python app.py
```

#### runtime.txt
```
python-3.13.7
```

### Pasos para Heroku:
1. Instala Heroku CLI
2. `heroku create tu-app-name`
3. `git push heroku main`

## 🔧 Opción 3: Railway

1. Ve a [railway.app](https://railway.app)
2. Conecta tu repositorio GitHub
3. Configura las variables de entorno
4. Despliega automáticamente

## 📱 Opción 4: Vercel (con adaptaciones)

Para Vercel necesitas crear un archivo `vercel.json`:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "./app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/"
    }
  ]
}
```

## 🐙 GitHub Pages (Solo Frontend)

Para una versión estática (sin backend), puedes convertir a GitHub Pages, pero perderías la funcionalidad de cálculo.

## ⚙️ Configuración para Producción

### Actualiza app.py para producción:

```python
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    print("🚀 Iniciando aplicación de Programación Lineal...")
    print("📊 Método Gráfico - Investigación de Operaciones")
    print(f"🌐 Servidor ejecutándose en puerto: {port}")
    print("-" * 50)
    
    app.run(debug=debug, host='0.0.0.0', port=port)
```

### Variables de entorno recomendadas:
- `DEBUG=False` (para producción)
- `PORT=5000` (o el que asigne la plataforma)
- `FLASK_ENV=production`

## 🔒 Consideraciones de Seguridad

1. **Cambia la secret_key en producción:**
   ```python
   app.secret_key = os.environ.get('SECRET_KEY', 'tu-clave-secreta-segura')
   ```

2. **Usa HTTPS en producción**

3. **Limita el tamaño de entrada** para evitar ataques

## 📊 Monitoreo y Logs

- Render y Heroku proporcionan logs automáticos
- Puedes agregar logging con Python:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# En tus rutas:
logger.info(f"Resolviendo problema LP: {objective}")
```

## 🎯 Recomendación Final

**Para tu proyecto académico, recomiendo Render** porque:
- ✅ Es gratuito
- ✅ Fácil de configurar
- ✅ Soporta Python sin problemas
- ✅ Proporciona HTTPS automático
- ✅ Tiene logs y monitoreo
- ✅ URL pública accesible desde cualquier dispositivo

¡Tu aplicación estará disponible 24/7 en internet!