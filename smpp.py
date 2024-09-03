import smpplib.client
import smpplib.consts

# Данные для подключения к SMPP серверу
# Замените на реальные данные вашего SMPP сервера
SMPP_SERVER = "YOUR_SMPP_SERVER_IP"  # IP-адрес или доменное имя SMPP сервера
SMPP_PORT = 2775  # Порт SMPP сервера (обычно 2775, но может отличаться)
SYSTEM_ID = "YOUR_SYSTEM_ID"  # Уникальный идентификатор системы, предоставленный SMPP провайдером
PASSWORD = "YOUR_PASSWORD"  # Пароль для аутентификации на SMPP сервере

# Функция для обработки входящих сообщений
def handle_message(pdu):
    print(f"Received message: {pdu.short_message.decode('utf-8')}")
    print(f"From: {pdu.source_addr}")
    print(f"To: {pdu.destination_addr}")

# Создаем клиента SMPP
client = smpplib.client.Client(SMPP_SERVER, SMPP_PORT)

# Включаем логирование (опционально)
client.set_message_received_handler(handle_message)

# Подключаемся и регистрируемся как приемник
client.connect()
client.bind_receiver(system_id=SYSTEM_ID, password=PASSWORD)

# Ждем входящих сообщений (асинхронно)
try:
    client.listen()  # client.listen() будет работать до тех пор, пока не получит сообщение или не произойдет ошибка
except KeyboardInterrupt:
    print("Disconnected from SMPP server.")

# Отключение от сервера
client.unbind()
client.disconnect()
