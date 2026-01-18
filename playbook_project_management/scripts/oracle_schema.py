import os
import oracledb

conn = oracledb.connect(
    user=os.environ["ORACLE_USER"],
    password=os.environ["ORACLE_PASSWORD"],
    host=os.environ["ORACLE_HOST"],
    port=int(os.environ["ORACLE_PORT"]),
    service_name=os.environ["ORACLE_SERVICE"]
)

cursor = conn.cursor()
print("Connection established.")

print(f"Setting current schema to {os.environ['ORACLE_USER']}")
cursor.execute(
    "ALTER SESSION SET CURRENT_SCHEMA = " + os.environ["ORACLE_USER"]
)
# 1️⃣ Get all table names and generate DROP statements
cursor.execute("""
    SELECT 'DROP TABLE "' || table_name || '" CASCADE CONSTRAINTS' AS drop_stmt FROM user_tables
""")

drop_statements = [row[0] for row in cursor.fetchall()]
print(f"Statements are {drop_statements}")

# 2️⃣ Execute DROP statements
for stmt in drop_statements:
    print(f"Executing: {stmt}")
    try:
        cursor.execute(stmt)
    except oracledb.DatabaseError as e:
        print(f"Error executing {stmt}: {e}")

conn.commit()

cursor.close()
conn.close()
print("Cursor and connection closed. Script finished successfully.")