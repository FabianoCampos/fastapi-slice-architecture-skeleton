
## Execução local

1. Criar um ambiente virtual
   ```bash
    poetry config virtualenvs.in-project true
    poetry install
   ```
   > Após a primeira execução não será necessário reexecutar o este passo

2. Ativar o ambiente virtual
   ```bash
   poetry shell
   ```

3. Instalar novas dependências
   ```bash
   poetry add <lib>
   ```
   ```bash
   poetry add <lib> --group dev
   ```

4. Subir o servidor local com uvicorn
   ```bash
   uvicorn app.main:app --port 8080 --reload
   ```


## Endpoints

**Swagger**: localhost:8080/docs   

**Redoc**: localhost:8080/redoc   

**Health Check**: localhost:8080/health   

**Demais endpoints**: localhost:8080/api/<feature>

## Testes

Executando todos os testes
```bash
pytest --cov=app ./tests
```

Gerando informações sobre cobertura de testes
```bash
pytest --cov=app --cov-report html
```


## Database Migrations

Gerando uma nova migração
```bash
alembic revision --autogenerate -m "Criando tabela departamento"
```

Atualizando estrutura 
```bash
alembic upgrade head
```

