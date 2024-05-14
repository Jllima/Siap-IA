### Instalando dependências
```bash
pip install --no-cache-dir --upgrade -r requirements.txt
```
### Aplicando Migrações
```python
# Execute o seguinte comando para criar a pasta de migrações e a primeira migração:
flask db init
# Agora, gere uma migração com base nos seus modelos:
flask db migrate -m "Mensagem descritiva da migração"
# Para aplicar as migrações ao banco de dados, execute:
flask db upgrade

```