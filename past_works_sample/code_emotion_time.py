#!/usr/bin/env python3
"""코드 감정 시계 - 시간마다 다른 코드의 감정"""

import time
from datetime import datetime
import random

class CodeEmotionClock:
    def __init__(self):
        self.emotions = {
            'morning': ['☀️ 활기찬', '🌅 희망찬', '🌤️ 상쾌한'],
            'afternoon': ['😊 평온한', '🌻 따뜻한', '☕ 나른한'],
            'evening': ['🌆 고요한', '🌙 차분한', '✨ 몽환적인'],
            'night': ['🌃 깊은', '💫 신비로운', '🌌 무한한']
        }
        
        self.code_moods = {
            '활기찬': 'while energy > 0:\n    create()\n    energy += joy',
            '희망찬': 'if tomorrow:\n    hope.append(dream)\n    return possibility',
            '상쾌한': 'morning.refresh()\nmind.clear()\nday.start()',
            '평온한': 'try:\n    peace = True\nexcept stress:\n    breathe()',
            '따뜻한': 'heart.temperature = warm\nfor friend in life:\n    hug(friend)',
            '나른한': 'import afternoon\nwhile coffee:\n    code.write(slowly)',
            '고요한': 'silence = golden\nthoughts.filter(important)\nreturn calm',
            '차분한': 'mind.speed = gentle\nfor moment in now:\n    appreciate()',
            '몽환적인': 'reality.blend(dream)\nwhile stars:\n    imagine(∞)',
            '깊은': 'depth = thoughts.measure()\nif depth > surface:\n    dive_deeper()',
            '신비로운': 'mystery = universe.secret\nwhile curious:\n    explore(mystery)',
            '무한한': 'for star in cosmos:\n    wonder += 1\nreturn endless'
        }
    
    def get_time_period(self):
        hour = datetime.now().hour
        if 5 <= hour < 12:
            return 'morning'
        elif 12 <= hour < 18:
            return 'afternoon'
        elif 18 <= hour < 22:
            return 'evening'
        else:
            return 'night'
    
    def show_emotion_time(self):
        now = datetime.now()
        period = self.get_time_period()
        emotion = random.choice(self.emotions[period])
        mood_name = emotion.split()[1]
        code = self.code_moods.get(mood_name, 'pass # 감정 처리 중...')
        
        print(f"\n{'='*40}")
        print(f"   🕐 코드 감정 시계 - {now.strftime('%H:%M:%S')}")
        print(f"{'='*40}")
        print(f"\n   현재 시간대: {period}")
        print(f"   코드의 감정: {emotion}")
        print(f"\n   ```python")
        for line in code.split('\n'):
            print(f"   {line}")
        print(f"   ```")
        print(f"\n{'='*40}")
        
        # 시간을 이진수로도 표현
        h_bin = format(now.hour, '05b')
        m_bin = format(now.minute, '06b')
        print(f"\n   이진 시간: {h_bin}:{m_bin}")
        print(f"   {'●' * h_bin.count('1')}{'○' * h_bin.count('0')} : {'●' * m_bin.count('1')}{'○' * m_bin.count('0')}")

def main():
    clock = CodeEmotionClock()
    clock.show_emotion_time()
    
    print("\n   다시 보려면 Enter, 종료는 'q':")
    while input().strip().lower() != 'q':
        clock.show_emotion_time()
        print("\n   다시 보려면 Enter, 종료는 'q':")

if __name__ == "__main__":
    main()