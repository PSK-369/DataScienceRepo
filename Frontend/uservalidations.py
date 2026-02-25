from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, field_validator, Field
from typing import List

app = FastAPI(title="auth form", version="1.0.0", summary="User authetication Form")


class userClass(BaseModel):
    username: str = Field(..., description="Username")
    password: str = Field(..., description="password")

    @field_validator("username")
    @classmethod
    def username_lengthcheck(cls, user: str):
        if len(user) <= 2:
            raise ValueError("username length is not matched")
        return user

    @field_validator("username")
    @classmethod
    def username_gmailcheck(cls, gmail: str):
        if "@gmail.com" in gmail:
            return gmail
        raise ValueError("@gmail.com is missed")

    @field_validator("password")
    @classmethod
    def password_lengthcheck(cls, pass1: str):
        if len(pass1) < 5:
            raise ValueError("password length is not matched < 5 you entered")
        return pass1

    @field_validator("password")
    @classmethod
    def password_qualitycheck(cls, pass2: str):
        has_lower = any(c in "abcdefghijklmnopqrstuvwxyz" for c in pass2)
        has_upper = any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in pass2)
        has_digit = any(c in "0123456789" for c in pass2)
        has_special = any(c in "!@#$^&*" for c in pass2)
        if has_lower and has_upper and has_digit and has_special:
            return pass2
        raise ValueError("password quanlity check is failed")


store: List[userClass] = []


@app.get("/")
def health_check():
    return {"healthcheck": "passed"}


@app.get("/username/{username}")
def username_present_check(username: str):
    for user in store:
        if username == user.username:
            return {"message": "username is already present"}
    raise HTTPException(status_code=404, detail="username is not present")


@app.delete("/username/{username}")
def delete_username(username: str):
    for idx, user in enumerate(store):
        if user.username == username:
            deleted = store.pop(idx)
            return {"message": "user deleted", "username": deleted.username}
    raise HTTPException(status_code=404, detail="user is not present")


@app.post("/username")
def login(credentials: userClass):
    if (
        credentials.username == "shravan123@gmail.com"
        or credentials.password == "Shravan123@"
    ):
        return {"message": "root credentails and login success"}
    else:
        for user in store:
            if (
                user.username == credentials.username
                and user.password == credentials.password
            ):
                return {"message": "login successful"}
    raise HTTPException(status_code=401, detail="invalid credentials")
