from fastapi import FastAPI

from src.app.models import GameState

app = FastAPI()


@app.get("/")
async def root():
    return {"detail": "Hello World"}


@app.get("/move")
async def move(game_state: GameState):
    return game_state


@app.post("/start")
async def start(game_state: GameState):
    return game_state

@app.post("/end")
async def end(game_state: GameState):
    return game_state
