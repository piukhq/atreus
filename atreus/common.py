import json
import logging
from pathlib import Path
from tempfile import NamedTemporaryFile

from azure.core.exceptions import ResourceNotFoundError, ServiceRequestError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

from atreus.settings import settings

logger = logging.getLogger(__name__)


def connect_to_vault() -> SecretClient:
    if settings.keyvault_url is None:
        raise Exception("Vault Error: settings.KEY_VAULT not set")

    try:
        return SecretClient(vault_url=settings.keyvault_url, credential=DefaultAzureCredential())
    except ResourceNotFoundError:
        logger.error("Could not connect to vault")


def _write_tmp_files(key: str, cert: str):
    paths = []
    for data in (key, cert):
        file = NamedTemporaryFile(delete=False)
        paths.append(file.name)
        file.write(data.encode())
        file.close()
    return tuple(paths)


def load_cert_from_vault(secret_name: str):
    client = connect_to_vault()
    client_cert_path = None
    client_priv_path = None

    try:
        client_priv_path, client_cert_path = _write_tmp_files(
            json.loads(client.get_secret(secret_name).value)["key"],
            json.loads(client.get_secret(secret_name).value)["cert"],
        )
    except ServiceRequestError:
        logger.error("Could not retrieve cert/key data from vault")

    return client_priv_path, client_cert_path


def _read_secret(key: str) -> str:
    try:
        path = Path(settings.secrets_path) / key
        try:
            with path.open() as f:
                return json.loads(f.read())
        except Exception:
            with path.open() as f:
                return f.read()
    except FileNotFoundError as e:
        logger.exception(e)
        raise
