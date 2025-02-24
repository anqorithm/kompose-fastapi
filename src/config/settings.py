from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Kompose FastAPI"
    app_version: str = "1.0.0"
    app_description: str = (
        "A FastAPI service that converts Docker Compose files to Kubernetes "
        "manifests using Kompose, to help you get started with container orchestration workflows"
    )
    app_env: str = "development"
    debug: bool = False
    api_prefix: str = "/api/v1"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
