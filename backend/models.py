from database import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY,
        product_name TEXT,
        stock INTEGER,
        reorder_level INTEGER
    )
    """)

    conn.commit()
    conn.close()
    