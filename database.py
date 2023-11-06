from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://pd9scoddorqa591cx6lk:pscale_pw_juW0NTyWCN6sJrG9fttioAI6bYZRulmcQnm8LbGCWAn@aws.connect.psdb.cloud/eco_cycle?charset=utf8mb4"

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