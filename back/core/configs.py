class Settings():
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://admin:admin@192.168.31.252:5432/postgres'

    class Config:
        case_sensitive = True


settings: Settings = Settings()
