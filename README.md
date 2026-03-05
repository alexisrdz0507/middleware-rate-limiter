# Middleware de Detección de Anomalías para APIs

Proyecto Integrador Dual - Ingeniería en Sistemas Computacionales

## Descripción
Middleware de rate limiting para proteger APIs REST contra ataques de fuerza bruta, 
scraping y DDoS a nivel de aplicación. Implementa algoritmo Token Bucket con Redis.

## Stack Tecnológico
- **Backend:** Python + FastAPI
- **Rate Limiting:** Algoritmo Token Bucket
- **Cache:** Redis (almacenamiento de tokens por IP)
- **Base de Datos:** PostgreSQL (logs históricos)
- **Simulación:** Python + Requests
- **Despliegue:** Render

## Estructura del Proyecto

1.- app/ # Código principal
    1.1 main.py # Punto de entrada
    1.2 middleware/ # Lógica de rate limiting
    1.3 models/ # Modelos de base de datos
    1.4 routes/ # Endpoints de prueba
    1.5utils/ # Utilidades (Redis, logger)
2.- scripts/ # Simulación de tráfico
3.- tests/ # Pruebas
4.- docs/ # Documentación
5.- logs/ # Archivos generados
6.- requirements.txt # Dependencias

## Instalación y Ejecución

1. **Clonar repositorio**
   ```bash
   git clone https://github.com/alexisrdz0507/middleware-rate-limiter.git
   cd middleware-rate-limiter

   
2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate

3. **Instalar dependencias**
   pip install -r requirements.txt

4. **Ejecutar servidor**
uvicorn app.main:app --reload

5. **Probar en navegador**

http://localhost:8000
http://localhost:8000/health

Prioridad ALTA (MVP Esencial)
ID	Historia de Usuario	Criterios de Aceptación
HU-01	Como administrador, quiero un middleware que intercepte todas las peticiones para aplicar rate limiting	• Middleware implementado antes de los endpoints
• Identificación de IP por petición
HU-02	Como desarrollador, quiero usar Redis para almacenar tokens por IP de forma atómica	• Conexión exitosa a Redis Cloud
• Operaciones INCR y EXPIRE funcionales
HU-03	Como administrador, quiero implementar Token Bucket para controlar tráfico	• Configurar MAX_TOKENS y REFILL_RATE
• Permitir ráfagas controladas
HU-04	Como administrador, quiero rechazar peticiones con HTTP 429 al exceder límite	• Respuesta automática con status 429
• Mensaje "Too Many Requests"
Prioridad MEDIA
ID	Historia de Usuario	Criterios de Aceptación
HU-05	Como científico de datos, quiero logs estructurados con métricas de rendimiento	• Archivo CSV con timestamp, CPU %, latencia
• Almacenamiento en PostgreSQL
HU-06	Como administrador, quiero un endpoint de prueba /api/data	• Endpoint funcional con latencia simulada
• Registro de peticiones
HU-07	Como desarrollador, quiero un script de simulación de tráfico	• 100 IPs normales (2-5 req/s)
• 10 IPs maliciosas (50-100 req/s)
Autor: Alexis

GitHub: @alexisrdz0507

## Proyecto Académico
Este proyecto es parte del Proyecto Integrador Dual de la carrera Ingeniería en Sistemas Computacionales.
