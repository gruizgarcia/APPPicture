import os

class Config:

    # ===== AWS =====
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    AWS_REGION     = os.getenv('AWS_REGION', 'us-east-1')
    S3_BUCKET      = os.getenv('S3_BUCKET', 'viko-evidencias')

    # ===== SAP =====
    SAP_URL        = os.getenv('SAP_URL')
    SAP_ENABLED    = os.getenv('SAP_ENABLED', 'false').lower() == 'true'

    # ===== GENERAL =====
    DEBUG          = os.getenv('DEBUG', 'true').lower() == 'true'