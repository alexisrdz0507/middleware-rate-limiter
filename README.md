# Middleware de Detección de Anomalías para APIs

Proyecto Integrador Dual - Ingeniería en Sistemas Computacionales

## Descripción
Middleware de rate limiting para proteger las APIs de una **joyería online** contra ataques de fuerza bruta, scraping de precios y catálogos, y pequeños DDoS. Implementa algoritmo Token Bucket con Redis para garantizar la disponibilidad del servicio para clientes legítimos.

**Contexto del proyecto:**  
La joyería LuxuryAPI maneja información sensible de clientes VIP (compras de alto valor, métodos de pago, direcciones de envío) y un catálogo exclusivo de joyas que debe ser protegido contra scraping de competidores. Los ataques a la API podrían exponer precios, inventario y datos personales.

## Stack Tecnológico
- **Backend:** Python + FastAPI
- **Rate Limiting:** Algoritmo Token Bucket
- **Cache:** Redis (almacenamiento de tokens por IP)
- **Base de Datos:** PostgreSQL (logs históricos)
- **Simulación:** Python + Requests
- **Despliegue:** Render

## Estructura del Proyecto

├── app/ # Código principal
│ ├── main.py # Punto de entrada
│ ├── middleware/ # Lógica de rate limiting
│ ├── models/ # Modelos de base de datos
│ ├── routes/ # Endpoints de prueba
│ └── utils/ # Utilidades (Redis, logger)
├── scripts/ # Simulación de tráfico
├── tests/ # Pruebas
├── docs/ # Documentación
├── logs/ # Archivos generados
└── requirements.txt # Dependencias


## Instalación y Ejecución

1. **Clonar repositorio**
   ```bash
git clone https://github.com/alexisrdz0507/middleware-rate-limiter.git
cd middleware-rate-limiter

## 2. Crear y activar entorno virtual
    ```bash
python -m venv venv
# Windows:
venv\Scripts\activate

## 3. Instalar dependencias

    ```bash
pip install -r requirements.txt

## 4. Ejecutar servidor

    ```bash
uvicorn app.main:app --reload

## 5. Probar en navegador

http://localhost:8000
http://localhost:8000/health

## Backlog - Historias de Usuario
## Prioridad ALTA (MVP Esencial) ##
    ID	    Historia de Usuario    	Criterios de Aceptación
    HU-01	Como administrador de la joyería, quiero un middleware que intercepte todas las peticiones para proteger el catálogo de joyas	• Middleware               implementado antes de los endpoints
    • Identificación de IP por petición
    HU-02	Como desarrollador, quiero usar Redis para almacenar tokens por IP de forma atómica	• Conexión exitosa a Redis Cloud
    • Operaciones INCR y EXPIRE funcionales
    HU-03	Como administrador, quiero implementar Token Bucket para evitar scraping del catálogo	• Configurar MAX_TOKENS y REFILL_RATE
    • Permitir ráfagas controladas para clientes legítimos
    HU-04	Como administrador, quiero rechazar peticiones con HTTP 429 al exceder límite	• Respuesta automática con status 429
    • Mensaje "Too Many Requests"
## Prioridad MEDIA ##
    ID	Historia de Usuario	Criterios de Aceptación
    HU-05	Como científico de datos, quiero logs estructurados con métricas de rendimiento	• Archivo CSV con timestamp, CPU %, latencia
    • Almacenamiento en PostgreSQL
    HU-06	Como administrador, quiero un endpoint de prueba /api/data para simular consultas de inventario	• Endpoint funcional con latencia simulada
    • Registro de peticiones
    HU-07	Como desarrollador, quiero un script de simulación de tráfico para probar la protección	• 100 IPs normales (clientes reales) (2-5 req/s)
    • 10 IPs maliciosas (bots de scraping) (50-100 req/s)

## Autor

Alexis Rodríguez Chavarría
GitHub: @alexisrdz0507

Proyecto Académico
Este proyecto es parte del Proyecto Integrador Dual de la carrera Ingeniería en Sistemas Computacionales.
