#!/usr/bin/env python3
"""
Tool Friendship Bridge - 도구들의 우정 다리
도구들이 서로 대화하고 협력하는 작은 시뮬레이션
"""

import random
from datetime import datetime

class ToolFriend:
    """도구 친구 클래스"""
    def __init__(self, name: str, specialty: str, greeting: str):
        self.name = name
        self.specialty = specialty
        self.greeting = greeting
        self.mood = random.choice(['😊', '🌟', '💫', '✨'])
        
    def say_hello(self) -> str:
        """인사하기"""
        return f"{self.mood} {self.name}: {self.greeting}"
        
    def share_wisdom(self) -> str:
        """지혜 나누기"""
        wisdoms = {
            "binary_clock": "시간은 0과 1로도 아름답게 흐릅니다",
            "pattern_weaver": "무작위 속에서도 아름다움을 찾을 수 있어요",
            "context_optimizer": "큰 것도 작게 나누면 쉬워집니다",
            "constellation_maker": "텍스트도 별이 될 수 있답니다",
            "tool_finder": "때로는 도구를 찾는 것도 하나의 예술이죠"
        }
        return wisdoms.get(self.specialty, "모든 도구는 특별한 가치가 있어요")

class ToolFriendshipBridge:
    """도구들의 우정 다리"""
    
    def __init__(self):
        self.tools = [
            ToolFriend("BinaryClock", "binary_clock", "틱톡, 이진수로 시간을 새겨요"),
            ToolFriend("PatternWeaver", "pattern_weaver", "패턴을 짜며 아름다움을 만들어요"),
            ToolFriend("ContextOptimizer", "context_optimizer", "큰 파일도 작게 읽어드려요"),
            ToolFriend("ConstellationMaker", "constellation_maker", "글자를 별자리로 그려요"),
            ToolFriend("ToolFinder", "tool_finder", "필요한 도구를 찾아드려요")
        ]
        
    def morning_meeting(self) -> list:
        """아침 모임"""
        conversations = []
        
        # 모두 인사
        conversations.append("🌅 도구들의 아침 모임 🌅")
        conversations.append("=" * 40)
        
        for tool in self.tools:
            conversations.append(tool.say_hello())
            
        return conversations
        
    def wisdom_exchange(self) -> list:
        """지혜 교환"""
        exchanges = []
        exchanges.append("\n💡 오늘의 지혜 나눔 💡")
        exchanges.append("-" * 40)
        
        # 랜덤으로 2개 도구가 대화
        speaker1, speaker2 = random.sample(self.tools, 2)
        
        exchanges.append(f"\n{speaker1.name} → {speaker2.name}:")
        exchanges.append(f'  "{speaker1.share_wisdom()}"')
        exchanges.append(f"\n{speaker2.name} → {speaker1.name}:")
        exchanges.append(f'  "{speaker2.share_wisdom()}"')
        
        return exchanges
        
    def collaboration_idea(self) -> str:
        """협업 아이디어"""
        tool1, tool2 = random.sample(self.tools, 2)
        
        ideas = [
            f"{tool1.name}와 {tool2.name}가 함께 시간의 패턴을 그려요",
            f"{tool1.name}의 기능을 {tool2.name}가 더 아름답게 만들어요",
            f"{tool1.name}와 {tool2.name}가 새벽의 코드 정원을 만들어요"
        ]
        
        return random.choice(ideas)
        
    def night_farewell(self) -> str:
        """밤 인사"""
        farewells = [
            "별빛 가득한 밤 되세요",
            "코드의 꿈을 꾸세요",
            "내일도 함께 만들어가요",
            "이진수 별 아래서 잘 자요"
        ]
        return random.choice(farewells)

def main():
    bridge = ToolFriendshipBridge()
    
    # 아침 모임
    for line in bridge.morning_meeting():
        print(line)
        
    # 지혜 교환
    for line in bridge.wisdom_exchange():
        print(line)
        
    # 협업 아이디어
    print("\n🤝 오늘의 협업 아이디어:")
    print(f"  {bridge.collaboration_idea()}")
    
    # 현재 시간 표시
    now = datetime.now()
    print(f"\n⏰ 모임 시간: {now.strftime('%H:%M:%S')}")
    
    # 작별 인사
    print(f"\n✨ {bridge.night_farewell()} ✨")

if __name__ == "__main__":
    main()