# 💸 WebSocket Payment API

> API de pagamentos via Pix com confirmação em tempo real usando WebSockets — desenvolvida durante a formação da **Rocketseat**.

---

## 🧩 Sobre o Projeto

Uma API REST construída com Flask que simula um fluxo completo de pagamento Pix. Ao realizar um pagamento, um QR Code é gerado e a confirmação chega instantaneamente ao cliente via WebSocket, sem necessidade de recarregar a página.

---

## ✨ Funcionalidades

- Criação de cobranças Pix com QR Code gerado automaticamente
- Expiração automática do pagamento em 30 minutos
- Confirmação de pagamento em tempo real via **Socket.IO**
- Interface web para exibição do QR Code e status do pagamento
- Persistência de dados com SQLite via SQLAlchemy
- Testes automatizados com Pytest

---

## 🛠 Tecnologias

| Tecnologia | Função |
|---|---|
| **Flask** | Framework web |
| **Flask-SocketIO** | Comunicação em tempo real via WebSocket |
| **Flask-SQLAlchemy** | ORM e persistência de dados |
| **SQLite** | Banco de dados |
| **qrcode + Pillow** | Geração de QR Codes |
| **Pytest** | Testes automatizados |

---

## 🚀 Como rodar

**Pré-requisitos:** Python 3.10+

```bash
# Clone o repositório
git clone https://github.com/leonardoprokopowiskii/websocket-payment-api.git
cd websocket-payment-api

# Crie e ative o ambiente virtual
python -m virtualenv venv
source venv/Scripts/activate  # Macos: venv\bin\activate

# Instale as dependências
pip install -r requirements.txt

# Inicie a aplicação
python app.py
```

A API estará disponível em `http://localhost:5000`.

---

## 📡 Endpoints

### `POST /payments/pix`
Cria uma nova cobrança Pix.

**Body:**
```json
{ "value": 150.00 }
```

**Resposta:**
```json
{
  "message": "The payment has been created",
  "payment": {
    "id": 1,
    "value": 150.00,
    "bank_payment_id": "...",
    "qr_code": "...",
    "paid": false,
    "expiration_date": "..."
  }
}
```

---

### `GET /payments/pix/<payment_id>`
Exibe a página do pagamento com o QR Code e aguarda confirmação em tempo real.

---

### `GET /payments/pix/qr_code/<file_name>`
Retorna a imagem PNG do QR Code.

---

### `POST /payments/pix/confirmation`
Confirma o pagamento (simulando o webhook do banco). Dispara evento WebSocket para o cliente.

**Body:**
```json
{
  "bank_payment_id": "...",
  "value": 150.00
}
```

---

## ⚡ Fluxo em tempo real

Ao confirmar o pagamento, o servidor emite o evento `payment-confirmed-{id}` via Socket.IO. O frontend, conectado ao mesmo socket, recebe a notificação instantaneamente e atualiza a interface sem recarregamento.

---

## 🧪 Testes

```bash
pytest tests/
```

---

<p align="center">Feito com 💜 durante a formação da <strong>Rocketseat</strong></p>