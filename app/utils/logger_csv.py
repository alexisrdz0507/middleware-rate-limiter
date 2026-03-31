import csv
import os
from datetime import datetime

LOG_FILE = "logs/metrics.csv"

class CSVLogger:
    def __init__(self):
        # Crear carpeta logs si no existe
        os.makedirs("logs", exist_ok=True)
        
        # Crear archivo con encabezados si no existe
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    "timestamp", "ip_address", "endpoint", 
                    "cpu_usage", "latency_ms", "requests_dropped", 
                    "action", "tokens_restantes"
                ])
            print("✅ Archivo logs/metrics.csv creado")
    
    def log(self, ip_address, endpoint, cpu_usage, latency_ms, 
            requests_dropped, action, tokens_restantes):
        """Guardar un registro en el CSV"""
        try:
            with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    datetime.now().isoformat(),
                    ip_address,
                    endpoint,
                    cpu_usage,
                    latency_ms,
                    requests_dropped,
                    action,
                    tokens_restantes
                ])
            return True
        except Exception as e:
            print(f"❌ Error guardando log: {e}")
            return False

# Instancia global
csv_logger = CSVLogger()