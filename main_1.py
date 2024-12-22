from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException, Body
# Создаем экземпляр приложения FastAPI
app = FastAPI()

messages_db = []

class Message(BaseModel):
    id: int = None
    text: str

@app.get("/")
async def get_all_messages()-> List[Message]:
    return messages_db

@app.get("/message/{message_id}")
async def get_messages(message_id: int) -> Message:
    try:
        return messages_db[message_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.post("/message")
async def create_message(message: Message) -> str:
    message.id = len(messages_db)
    messages_db.append(message)
    return "Сообщение успешно добавлено"

@app.put("/message/{message_id}")
async def update_message(message_id: int, message:str = Body()) -> str:
    try:
        edit_messages = messages_db[message_id]
        edit_messages.text = message
        return "Сообщение изменено "
    except IndexError:
        raise HTTPException(status_code=404, detail="Сообщение не добавлено")

@app.delete("/message/{message_id}")
async def delete_message(message_id: int) -> str:
    try:
        messages_db.pop(message_id)
        return f"Соообщение с id {message_id} удалено"
    except IndexError:
        raise HTTPException(status_code=404, detail=f"Сообщение отсутствует по id № {message_id} ")


@app.delete("/")
async def delete_all_messages(message_id: int) -> str:
    try:
        messages_db.pop(message_id)
        return f"Сообщение с id {message_id} удаленно"
    except IndexError:
        raise HTTPException(status_code=404, detail=f"Сообщение с id {message_id} отсутствует")
