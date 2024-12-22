from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException, Body
# Создаем экземпляр приложения FastAPI
app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
async def get_all_messages()-> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def get_users(id: int, user: str, age: int) -> str:
    if len(users) == 0:
        new_id = 1  # Если список пуст, назначаем ID 1
    else:
        new_id = max(user.id for user in users) + 1
    users.append(User(id=new_id, username=user, age=age))
    return f"Пользователь {id},{user}, возраст {age} лет(год) успешно добавлен"
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
      for user in users:
            if user.id == user_id:
                user.age = age
                user.username = username
                return f"Пользователь id № {user_id} изменен на {username},возраст {age} лет(год)"

            raise HTTPException(status_code=404, detail="Пользователь не найден ")

@app.delete("/user/{user_id}")
async def delete_message(user_id: int) -> str:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return f"Пользователь с id {user_id} удален "
    raise HTTPException(status_code=404, detail=f"Пользователь отсутствуетт по id № {user_id} ")


