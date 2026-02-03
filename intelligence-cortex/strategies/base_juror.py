from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

class VoteDirection(Enum):
    LONG = 1
    SHORT = -1
    NEUTRAL = 0

@dataclass
class JurorVerdict:
    juror_id: str
    direction: VoteDirection
    confidence: float
    rationale: str

class StrategyJuror(ABC):
    def __init__(self, strategy_id: str):
        self.strategy_id = strategy_id

    @abstractmethod
    async def analyze(self, market_data: dict) -> JurorVerdict:
        pass
