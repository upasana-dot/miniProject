from database import get_connection
# def get_inventory():
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM inventory")
#     rows = cursor.fetchall()
#     inventory_list = []
#     for row in rows:
#         product_id, name, stock, reorder = row
#         status = "Reorder" if stock < reorder else "Optimal"
#         inventory_list.append({
#             "id": product_id,
#             "product": name,
#             "stock": stock,
#             "reorder_level": reorder,
#             "status": status
#         })
#     conn.close()
#     return inventory_list
# # def get_inventory():
# #     return [
# #         {"product": "Product A", "stock": 120, "status": "Reorder"},
# #         {"product": "Product B", "stock": 300, "status": "Optimal"}
# #     ]

def calculate_reorder(stock, avg_demand, lead_time=5, safety_stock=20):
    reorder_level = (avg_demand * lead_time) + safety_stock
    return reorder_level


def get_inventory():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()

    inventory_list = []

    for row in rows:
        product_id, name, stock, reorder = row

        avg_demand = 10  # Example demand (later connect ML)
        new_reorder = calculate_reorder(stock, avg_demand)

        status = "Reorder" if stock < new_reorder else "Optimal"

        inventory_list.append({
            "product": name,
            "stock": stock,
            "calculated_reorder_level": new_reorder,
            "status": status
        })

    conn.close()
    return inventory_list