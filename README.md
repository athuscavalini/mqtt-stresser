# MQTT Stresser

Um ambiente para fazer teste de carga e compreender o uso do protocolo MQTT. 

## Conteúdo:

### Scripts básicos:
- `client.py` Define o cliente MQTT utilizando as configurações pré estabelecidas no arquivo.
- `sub.py` Subscreve em um tópico e loga o tamanho das mensagens recebidas.
- `pub.py` Faz uma publicação em um tópico usando texto plano.
  
### Scripts específicos:
- `payload.py` Publica mensagens a cada 0.1s aumentando o tamanho da mensagem em 100.000 caracateres a cada publicação.
- `frequency.py` Publica 10 mensagens por segundo (de 100 caracteres cada).
- `multiple_pubs.py` Chama um novo publisher de `frequency.py` (thread) a cada 5 segundos.
- `multiple_subs.py` Cria um novo subscriber `sub.py` (thread) a cada 5 segundos.


## Uso

1. Instalar Mosquitto
```
sudo apt-get install mosquitto mosquitto-clients
```

2. O broker vai ser inicializado por padrão.  É necessário pará-lo e reinicializá-lo.

```
sudo /etc/init.d/mosquitto restart
```

3. Configure o broker e tópico em `client.py`, se necessário.

4. Instale as dependências do arquivo `requirements.txt`:

```
pip3 install -r requirements.txt
```

5. Execute os arquivos em terminais diferentes de acordo com os testes que se deseja realizar.
