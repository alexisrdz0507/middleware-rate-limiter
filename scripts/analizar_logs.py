import pandas as pd
import numpy as np
from scipy import stats
import os

# Ruta del archivo de logs
LOG_FILE = "logs/metrics.csv"

def analizar_logs():
    if not os.path.exists(LOG_FILE):
        print("❌ No se encontró el archivo de logs")
        return
    
    # Leer datos
    df = pd.read_csv(LOG_FILE)
    print(f"📊 Total de registros: {len(df)}")
    print(f"📊 Columnas: {list(df.columns)}")
    
    # Separar por acción
    allowed = df[df['action'] == 'ALLOWED']
    blocked = df[df['action'] == 'BLOCKED']
    
    print(f"\n✅ Peticiones permitidas: {len(allowed)}")
    print(f"❌ Peticiones bloqueadas: {len(blocked)}")
    
    # Estadísticas de CPU
    print("\n📈 ESTADÍSTICAS DE CPU:")
    print(f"   CPU promedio (permitidas): {allowed['cpu_usage'].mean():.2f}%")
    print(f"   CPU promedio (bloqueadas): {blocked['cpu_usage'].mean():.2f}%")
    print(f"   Reducción: {allowed['cpu_usage'].mean() - blocked['cpu_usage'].mean():.2f}%")
    
    # Estadísticas de latencia
    print("\n⏱️ ESTADÍSTICAS DE LATENCIA:")
    print(f"   Latencia promedio (permitidas): {allowed['latency_ms'].mean():.0f} ms")
    print(f"   Latencia promedio (bloqueadas): {blocked['latency_ms'].mean():.0f} ms")
    
    # Prueba t-Student
    if len(allowed) > 1 and len(blocked) > 1:
        t_stat, p_value = stats.ttest_ind(allowed['cpu_usage'], blocked['cpu_usage'])
        print(f"\n📊 PRUEBA t-STUDENT (CPU):")
        print(f"   t-statistic: {t_stat:.4f}")
        print(f"   p-value: {p_value:.4f}")
        
        if p_value < 0.05:
            print(f"   ✅ Diferencia SIGNIFICATIVA (p < 0.05)")
            print(f"   ✅ HIPÓTESIS VALIDADA: Rate limiting reduce CPU")
        else:
            print(f"   ⚠️ Diferencia NO SIGNIFICATIVA (p >= 0.05)")
    
    # Resumen
    print("\n" + "="*50)
    print("📋 RESUMEN:")
    print(f"   Total peticiones: {len(df)}")
    print(f"   Tasa de bloqueo: {(len(blocked)/len(df)*100):.1f}%")
    print(f"   Reducción de CPU: {(allowed['cpu_usage'].mean() - blocked['cpu_usage'].mean()):.2f}%")

if __name__ == "__main__":
    analizar_logs()