import psutil

# Obtener estadísticas de la CPU
cpu_stats = psutil.cpu_stats()

print("CPU Stats:")
print("----------")
print(f"Tiempo de usuario: {cpu_stats.user} segundos")
print(f"Tiempo de sistema: {cpu_stats.system} segundos")
print(f"Tiempo de inactividad: {cpu_stats.idle} segundos")
print(f"Tiempo de espera: {cpu_stats.iowait} segundos")

# Obtener porcentaje de uso de la CPU
cpu_percent = psutil.cpu_percent(interval=1, percpu=True)

print("\nUso de la CPU por núcleo:")
print("--------------------------")
for i, percent in enumerate(cpu_percent):
    print(f"Núcleo {i}: {percent}%")

# Obtener información detallada de cada núcleo de la CPU
cpu_info = psutil.cpu_times(percpu=True)

print("\nInformación detallada de la CPU:")
print("--------------------------------")
for i, info in enumerate(cpu_info):
    print(f"Núcleo {i}:")
    print(f"    Tiempo de usuario: {info.user} segundos")
    print(f"    Tiempo de sistema: {info.system} segundos")
    print(f"    Tiempo de inactividad: {info.idle} segundos")
    print(f"    Tiempo de espera: {info.iowait} segundos")
