from typing import List

from pydantic import BaseModel

class RulesetSettings(BaseModel):
    food_spawn_chance: int
    minimum_food: int
    hazard_damage_per_turn: int

class Ruleset(BaseModel):
    name: str
    version: str
    ruleset: RulesetSettings

class Game(BaseModel):
    id: str
    ruleset:Ruleset
    map: str
    source: str
    timeout: int

class SnakeCustomisations(BaseModel):
    colour: str
    head: str
    tail: str


class Location(BaseModel):
    x: int
    y: int


class Battlesnake(BaseModel):
    id: str
    name: str
    health: int
    body: List[Location]
    latency: str
    head: Location
    length: int
    shout: str
    customisations: SnakeCustomisations

class Board(BaseModel):
    height: int
    width: int
    food: List[Location]
    hazard: List[Location]
    snakes: List[Battlesnake]
    you: Battlesnake

class GameState(BaseModel):
    game: Game
    turn: int
    board: Board

