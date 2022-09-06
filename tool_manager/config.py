from pathlib import Path


class Settings:
    HOST: str = 'localhost'
    DATABASE: str = 'tool-manager'
    USER: str = 'root'
    PASSWORD: str = 'tool-manager'

    class Config:
        env_file = Path(__file__).parents[1] / '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
