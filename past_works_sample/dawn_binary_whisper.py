#!/usr/bin/env python3
"""
Dawn Binary Whisper - 새벽의 이진 속삭임
새벽 시간의 고요함을 이진수로 표현하는 작은 장난감
"""

import time
import random
from datetime import datetime

class DawnBinaryWhisper:
    def __init__(self):
        self.dawn_hours = list(range(3, 7))  # 3AM - 6AM
        self.whispers = {
            '00000': '·····',  # silence
            '00001': '☆····',  # first star
            '00010': '··☽··',  # moon glow
            '00011': '☆·☽··',  # star and moon
            '00100': '···◦·',  # dewdrop
            '00101': '☆··◦·',  # star and dew
            '00110': '··☽◦·',  # moon and dew
            '00111': '☆·☽◦·',  # all three
            '01000': '····❋',  # frost
            '01001': '☆···❋',  # star frost
            '01010': '··☽·❋',  # moon frost
            '01011': '☆·☽·❋',  # celestial frost
            '01100': '···◦❋',  # dew frost
            '01101': '☆··◦❋',  # morning magic
            '01110': '··☽◦❋',  # lunar dew
            '01111': '☆·☽◦❋',  # full dawn
            '10000': '~~~~~',  # mist
            '10001': '☆~~~~',  # starry mist
            '10010': '~~☽~~',  # moonlit mist
            '10011': '☆~☽~~',  # celestial mist
            '10100': '~~~◦~',  # misty dew
            '10101': '☆~~◦~',  # star dew mist
            '10110': '~~☽◦~',  # moon dew mist
            '10111': '☆~☽◦~',  # morning trinity
            '11000': '~~~~❋',  # frost mist
            '11001': '☆~~~❋',  # frozen stars
            '11010': '~~☽~❋',  # frozen moon
            '11011': '☆~☽~❋',  # frozen sky
            '11100': '~~~◦❋',  # frozen dew
            '11101': '☆~~◦❋',  # dawn crystal
            '11110': '~~☽◦❋',  # lunar crystal
            '11111': '☆~☽◦❋'   # perfect dawn
        }
        
    def time_to_binary(self):
        """현재 시간을 이진수로"""
        now = datetime.now()
        hour_bin = format(now.hour, '05b')
        min_bin = format(now.minute, '06b')
        sec_bin = format(now.second, '06b')
        return hour_bin, min_bin, sec_bin
    
    def whisper_pattern(self, binary_str):
        """이진수를 속삭임 패턴으로"""
        pattern = []
        for i in range(0, len(binary_str), 5):
            chunk = binary_str[i:i+5].ljust(5, '0')
            pattern.append(self.whispers.get(chunk, '·····'))
        return ' '.join(pattern)
    
    def dawn_meditation(self):
        """새벽 명상"""
        print("\n✨ Dawn Binary Whisper ✨")
        print("═" * 40)
        
        hour, minute, second = self.time_to_binary()
        current_hour = datetime.now().hour
        
        if current_hour in self.dawn_hours:
            print(f"\n🌅 Perfect dawn hour: {current_hour}:00")
        else:
            print(f"\n🌙 Current hour: {current_hour}:00")
        
        print(f"\nTime in binary:")
        print(f"  Hour:   {hour}")
        print(f"  Minute: {minute}")
        print(f"  Second: {second}")
        
        # 시간을 속삭임으로
        full_binary = hour + minute + second
        whisper = self.whisper_pattern(full_binary)
        
        print(f"\nDawn whisper pattern:")
        print(f"  {whisper}")
        
        # 애니메이션 효과
        print("\n🌠 Listening to dawn...")
        for i in range(5):
            bits = ''.join(random.choice('01') for _ in range(5))
            pattern = self.whispers.get(bits, '·····')
            print(f"\r  {pattern}", end='', flush=True)
            time.sleep(0.5)
        
        # 새벽 하이쿠
        self.create_dawn_haiku()
        
    def create_dawn_haiku(self):
        """새벽 하이쿠 생성"""
        print("\n\n📜 Dawn Binary Haiku:")
        
        binary_moment = format(random.randint(0, 31), '05b')
        whisper = self.whispers.get(binary_moment, '·····')
        
        haiku = f"""
  {binary_moment} whispers
  {whisper} in the dawn light
  Binary silence
        """
        print(haiku)
        
        # 최종 메시지
        if datetime.now().hour in self.dawn_hours:
            print("\n🌟 The dawn speaks in binary whispers...")
        else:
            print("\n💫 Every hour has its own binary song...")

def main():
    whisper = DawnBinaryWhisper()
    whisper.dawn_meditation()
    
    print("\n✨ May your dawn be filled with peaceful whispers ✨")

if __name__ == "__main__":
    main()