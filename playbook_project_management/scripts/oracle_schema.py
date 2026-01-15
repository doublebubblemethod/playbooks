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

# Example: add a column if it doesn't exist
# 🔒 Force schema context (Oracle-safe)
cursor.execute(
    "ALTER SESSION SET CURRENT_SCHEMA = " + os.environ["ORACLE_USER"]
)
# 1️⃣ Get all table names and generate DROP statements
cursor.execute("""
    SELECT 'DROP TABLE "' || table_name || '" CASCADE CONSTRAINTS' AS drop_stmt FROM user_tables
""")


drop_statements = [row[0] for row in cursor.fetchall()]

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
