import os


class Config:
    SECRET_KEY = 'lkasjdf09ajsdkfljalsiorj12n3490re9485309irefvn,u90818734902139489230'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLAlchemy 1.4 no longer supports url strings that start with 'postgres'
    # (only 'postgresql') but heroku's postgres add-on automatically sets the
    # url in the hidden config vars to start with postgres.
    # so the connection uri must be updated here
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres.chjkmylljokmkpnotpqw:diiUL7yxVyGnpjJL@aws-0-ap-south-1.pooler.supabase.com:5432/postgres'
    SQLALCHEMY_ECHO = True
    S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
    S3_KEY = os.environ.get("S3_ACCESS_KEY")
    S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
    S3_LOCATION = f"http://{S3_BUCKET}.s3.amazonaws.com/"
    MAPS_API_KEY = os.environ.get('MAPS_API_KEY')
