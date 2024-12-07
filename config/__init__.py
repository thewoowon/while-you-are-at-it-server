import os

ENV = os.getenv("ENV", "development")  # 기본값은 development

if ENV == "development":
    from .development import *
elif ENV == "production":
    from .production import *
else:
    raise ValueError(f"Unknown environment: {ENV}")
