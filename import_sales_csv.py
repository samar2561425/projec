import pandas as pd
import sqlite3

# اقرأ ملف CSV (تأكد أن المسار صحيح)
csv_path = "sales_5000.csv"
df = pd.read_csv(csv_path)

# اتصل بقاعدة بيانات SQLite (أو أنشئها لو ما كانت موجودة)
conn = sqlite3.connect("sales_project.db")

# احفظ البيانات في جدول اسمه 'sales'
df.to_sql('sales', conn, if_exists='replace', index=False)

print("Database created and data imported successfully.")

conn.close()
