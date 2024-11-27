import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"  # Cambia esto si usas un servidor remoto
    "DATABASE=LigaDeportiva;"
    "UID=;"  # Usuario SQL
    "PWD=;"
    "TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(conn_str)
    print("Conexión exitosa.")
except Exception as e:
    print(f"Error al conectar: {e}")
