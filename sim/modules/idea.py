# sim/modules/idea.py

"""
데이터 클래스 정의: 아이디어 객체
"""

from dataclasses import dataclass, field
import random

@dataclass
class Idea:
    """시뮬레이션에서 다루는 아이디어 객체.

    - `content`: 아이디어 텍스트 (예시 문자열)
    - `author_id`: 생성한 에이전트 ID
    - `adoption_rate`: 현재 채택 비율 (0~1)
    - `spread_rate`: 전파 속도 (시뮬레이션 단계당 증가량)
    - `quality`: 품질 점수 (0~1)
    - `status`: 현재 상태 ("active", "rejected", "integrated")
    """
    content: str = ""
    author_id: int = 0
    adoption_rate: float = 0.0
    spread_rate: float = 0.1
    quality: float = field(default_factory=lambda: random.random())
    status: str = "active"

    def step(self):
        """시간 흐름에 따라 전파와 채택을 업데이트한다."""
        self.adoption_rate = min(1.0, self.adoption_rate + self.spread_rate)
