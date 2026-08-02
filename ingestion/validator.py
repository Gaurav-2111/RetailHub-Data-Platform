TABLE_CONFIG = {

    "customers": {
        "required_columns": [
            "customer_id",
            "customer_unique_id",
            "customer_zip_code_prefix",
            "customer_city",
            "customer_state",
        ],
        "primary_key": []
    },

    "geolocation": {
        "required_columns": [
            "geolocation_zip_code_prefix",
            "geolocation_lat",
            "geolocation_lng",
            "geolocation_city",
            "geolocation_state",
        ],
        "primary_key": []
    },

    "order_items": {
        "required_columns": [
            "order_id",
            "order_item_id",
            "product_id",
            "seller_id",
            "shipping_limit_date",
            "price",
            "freight_value",
        ],
        "primary_key": []
    },

    "order_payments": {
        "required_columns": [
            "order_id",
            "payment_sequential",
            "payment_type",
            "payment_installments",
            "payment_value",
        ],
        "primary_key": []
    },

    "orders": {
        "required_columns": [
            "order_id",
            "customer_id",
            "order_status",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ],
        "primary_key": []
    },

    "product_category_name_translation": {
        "required_columns": [
            "product_category_name",
            "product_category_name_english",
        ],
        "primary_key": []
    },

    "products": {
        "required_columns": [
            "product_id",
            "product_category_name",
            "product_name_lenght",
            "product_description_lenght",
            "product_photos_qty",
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm",
        ],
        "primary_key": []
    },

    "reviews": {
        "required_columns": [
            "review_id",
            "order_id",
            "review_score",
            "review_comment_title",
            "review_comment_message",
            "review_creation_date",
            "review_answer_timestamp",
        ],
        "primary_key": []
    },

    "sellers": {
        "required_columns": [
            "seller_id",
            "seller_zip_code_prefix",
            "seller_city",
            "seller_state",
        ],
        "primary_key": []
    }
}


def validate(df , table):
    # Check for expected columns
    

    table = table.lower()  # Convert table name to lowercase for case-insensitive comparison
    if table not in TABLE_CONFIG:
        raise ValueError(f"Table '{table}' is not supported.")

    expected_columns = set(TABLE_CONFIG[table]["required_columns"])
    primary_key = TABLE_CONFIG[table]["primary_key"]



    actual_columns = set(df.columns)
    missing_columns = expected_columns - actual_columns

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError(f"{table} dataset is empty.")

    # Check for missing values in the primary key column
    if primary_key and df[primary_key].isnull().any().any():
        raise ValueError(f"Primary key '{primary_key}' contains null values.")

    # Check for duplicate values in the primary key column
    if primary_key and df[primary_key].duplicated().any():
        raise ValueError(f"Primary key '{primary_key}' contains duplicate values.")
        

    return df