import hvac
from kubernetes import config as kube_config


class VaultClient:
    def __init__(self, vault_endpoint, vault_k8s_role, vault_mount_point):
        # Carrega as configurações do cluster Kubernetes
        kube_config.load_incluster_config()

        # Obtém o token de serviço do Kubernetes para autenticação no Vault
        token_file = "/var/run/secrets/kubernetes.io/serviceaccount/token"
        with open(token_file, "r") as f:
            token = f.read()

        # Configura o cliente do Vault
        self.client = hvac.Client(url=vault_endpoint, token=token)

        # Realiza a autenticação do cliente no Vault
        self.client.auth_kubernetes(role=vault_k8s_role, jwt=token)

        self.vault_mount_point = vault_mount_point

    def read_secret(self, secret_path, secret_key):
        # Lê valor da secret do Vault
        secret_value = self.client.secrets.kv.v2.read_secret_version(
            mount_point=self.vault_mount_point, path=secret_path
        )["data"]["data"][secret_key]

        return secret_value
