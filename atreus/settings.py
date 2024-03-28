from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    keyvault_url: str = ""
    visa_auth_token: str = ""
    visa_community_code: str = "BINK"
    amex_auth_token: str = ""
    amex_hostname: str = "https://apigateway2s.americanexpress.com"
    stonegate_atreemo_url: str = "https://rihanna.atreemo.uk"
    secrets_path: str = "/mnt/secrets"
    auth: str = ""
    givex_number: str = ""


settings = Settings()
