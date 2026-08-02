from loader import loader_csv
from validator import validate
from load import load
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="pipeline.log",
    filemode="a",
    force = True
)

csv_files = [
    'Data/customers_dataset.csv',
    'Data/orders_dataset.csv',
    'Data/products_dataset.csv',
    'Data/geolocation_dataset.csv',
    'Data/sellers_dataset.csv',
    'Data/product_category_name_translation.csv',
    'Data/order_items_dataset.csv',
    'Data/olist_order_payments_dataset.csv',
    'Data/order_reviews_dataset.csv'
]

TABLE_NAMES = {
    'Data/customers_dataset.csv': 'customers',
    'Data/orders_dataset.csv': 'orders',
    'Data/products_dataset.csv': 'products',
    'Data/geolocation_dataset.csv': 'geolocation',
    'Data/sellers_dataset.csv': 'sellers',
    'Data/product_category_name_translation.csv': 'product_category_name_translation',
    'Data/order_items_dataset.csv': 'order_items',
    'Data/olist_order_payments_dataset.csv': 'order_payments',
    'Data/order_reviews_dataset.csv': 'reviews',
}

for file in csv_files:
    try:
        logging.info(f"Processing file: {file}")
        df = loader_csv(file)
        table = TABLE_NAMES[file]

        validated_df = validate(df, table)

        load(validated_df, table)
        logging.info(f"Validation successful for file: {file}")
    except ValueError as e:
        logging.error(f"Error occurred while processing file: {file}. Error: {e}")
        break
    except Exception as e:
        logging.error(f"Loading failed: {e}")
        break
