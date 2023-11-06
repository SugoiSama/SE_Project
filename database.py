from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']


engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_product_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM product"))

    productss = []
    for row in result.all():
        productss.append(dict(row._asdict()))  # Use row._asdict() to convert to a dictionary
    return productss