#!/usr/bin/env python3
"""이진 시간 꽃 - 시간을 이진수로 표현하는 꽃"""

import time
from datetime import datetime

def time_to_binary_flower():
    """현재 시간을 이진수 꽃으로 표현"""
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    
    # 시간을 이진수로 변환
    h_bin = format(hour, '05b')
    m_bin = format(minute, '06b')
    s_bin = format(second, '06b')
    
    # 꽃 그리기
    print("\n" + " " * 10 + "🌸 이진 시간 꽃 🌸")
    print(" " * 15 + f"{hour:02d}:{minute:02d}:{second:02d}")
    print()
    
    # 꽃잎 (시간)
    print(" " * 14 + "  ∧__∧  ")
    print(" " * 14 + f" ( {h_bin} )")
    print(" " * 14 + "  ￣￣￣  ")
    
    # 줄기와 잎 (분)
    print(" " * 16 + " | ")
    print(" " * 12 + f"🍃 {m_bin} 🍃")
    print(" " * 16 + " | ")
    
    # 뿌리 (초)
    print(" " * 11 + f"🌱 {s_bin} 🌱")
    print()
    
    # 이진수 해석
    print(" " * 5 + f"시: {'●'*h_bin.count('1')}{'○'*h_bin.count('0')} ({hour})")
    print(" " * 5 + f"분: {'●'*m_bin.count('1')}{'○'*m_bin.count('0')} ({minute})")
    print(" " * 5 + f"초: {'●'*s_bin.count('1')}{'○'*s_bin.count('0')} ({second})")

def animate_flower():
    """꽃이 시간에 따라 피고 지는 애니메이션"""
    try:
        while True:
            print("\033[2J\033[H")  # 화면 지우기
            time_to_binary_flower()
            print("\n" + " " * 5 + "Ctrl+C로 종료")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🌺 꽃이 잠들었습니다... 🌺")

if __name__ == "__main__":
    print("정적 보기는 Enter, 애니메이션은 'a' 입력:")
    choice = input().strip().lower()
    
    if choice == 'a':
        animate_flower()
    else:
        time_to_binary_flower()