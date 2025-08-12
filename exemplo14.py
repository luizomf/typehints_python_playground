#
# a
#


class DatabaseConfig:
    def __init__(self, dns: str) -> None:
        self._dns = dns

    @property
    def dsn(self) -> str:
        return self._dns


class MySqlDatabaseConfig(DatabaseConfig):
    def __init__(self, host: str, user: str, password: str, db: str) -> None:
        # Não tem DSN, vai tentar usar os dados abaixo
        self.host = host
        self.user = user
        self.password = password
        self.db = db

        # Exemplo clássico onde o dev forçou "É um" paga "pegar"
        # Métodos já definidos na classe base
        super().__init__("")  # Só para inicializar corretamente


def connect(cfg: DatabaseConfig) -> None:
    # Cliente depende da invariante DatabaseConfig.url
    print("Connecting to:", cfg.dsn)

    # ❌ Mas está vazia, ou quebra abaixo ou segue pra quebrar adiante
    # driver.connect(cfg.url)


cfg_bad = MySqlDatabaseConfig(host="", user="root", password="", db="app")
connect(cfg_bad)  # ❌ imprime url vazia; se já não tiver quebrado antes
