from pydantic.env_settings import BaseSettings
from pydantic.types import SecretStr


class Config(BaseSettings):
    # YNAB
    bearer_id: SecretStr = SecretStr("123")
    budget_id: str = "123"
    splitwise_id: str = "123"

    # Splitwise
    splitwise_consumer_key: SecretStr = SecretStr("123")
    splitwise_consumer_secret: SecretStr = SecretStr("123")
    splitwise_api_key: SecretStr = SecretStr("123")
