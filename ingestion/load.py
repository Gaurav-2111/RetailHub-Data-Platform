from database import get_connection


INSERT_QUERIES = {
    "customers": """INSERT INTO customers
        (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state)
        VALUES (%s, %s, %s, %s, %s)""",
    "geolocation": """INSERT INTO geolocation
        (geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state)
        VALUES (%s, %s, %s, %s, %s)""",
    "order_items": """INSERT INTO order_items
        (order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value)
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
    "order_payments": """INSERT INTO order_payments
        (order_id, payment_sequential, payment_type, payment_installments, payment_value)
        VALUES (%s, %s, %s, %s, %s)""",
    "orders": """INSERT INTO orders
        (order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at,
         order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
    "product_category_name_translation": """INSERT INTO product_category_name_translation
        (product_category_name, product_category_name_english)
        VALUES (%s, %s)""",
    "products": """INSERT INTO products
        (product_id, product_category_name, product_name_lenght, product_description_lenght,
         product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
    "sellers": """INSERT INTO sellers
        (seller_id, seller_zip_code_prefix, seller_city, seller_state)
        VALUES (%s, %s, %s, %s)""",
    "reviews": """INSERT INTO reviews
        (review_id, order_id, review_score, review_comment_title, review_comment_message,
         review_creation_date, review_answer_timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
}


def load(df, table):
    table = table.lower()
    if table not in INSERT_QUERIES:
        raise ValueError(f"Table '{table}' is not supported.")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        data = list(df.itertuples(index=False, name=None))
        cursor.executemany(INSERT_QUERIES[table], data)
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()

