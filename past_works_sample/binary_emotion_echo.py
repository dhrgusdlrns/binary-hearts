#!/usr/bin/env python3
"""
Binary Emotion Echo - 이진 감정 메아리
감정을 이진수로 변환하고 패턴으로 울려 퍼지게 합니다
"""
import time
import random

emotions = {
    "기쁨": "😊",
    "사랑": "💕", 
    "평화": "🕊️",
    "놀람": "😮",
    "생각": "🤔",
    "꿈": "💭",
    "빛": "✨",
    "밤": "🌙"
}

def text_to_binary(text):
    """텍스트를 이진수로 변환"""
    return ' '.join(format(ord(c), '08b') for c in text)

def create_echo_pattern(binary_str, depth=3):
    """이진수를 메아리 패턴으로 변환"""
    echoes = []
    current = binary_str.replace(' ', '')
    
    for i in range(depth):
        # 페이드 효과
        fade_level = depth - i
        pattern = ''
        
        for bit in current:
            if bit == '1':
                pattern += '█' * fade_level
            else:
                pattern += '·' * fade_level
            pattern += ' '
        
        echoes.append(pattern)
        
        # 다음 메아리를 위한 변형
        current = current[1:] + current[0]  # 회전
    
    return echoes

def main():
    print("🌊 이진 감정 메아리 🌊")
    print("감정이 이진수로 울려 퍼집니다...")
    print("=" * 40)
    
    # 랜덤 감정 선택
    emotion_name = random.choice(list(emotions.keys()))
    emotion_icon = emotions[emotion_name]
    
    print(f"\n오늘의 감정: {emotion_icon} {emotion_name}")
    
    # 이진수 변환
    binary = text_to_binary(emotion_name)
    print(f"이진수: {binary}")
    
    # 메아리 생성
    echoes = create_echo_pattern(binary)
    
    print("\n메아리가 퍼집니다...")
    time.sleep(1)
    
    for i, echo in enumerate(echoes):
        print(f"\n[메아리 {i+1}]")
        print(echo)
        time.sleep(0.5)
    
    # 감정 메시지
    messages = {
        "기쁨": "기쁨은 이진수로도 반짝입니다",
        "사랑": "사랑은 0과 1 사이에도 있어요",
        "평화": "평화로운 비트가 흐릅니다",
        "놀람": "놀라운 패턴이 나타났네요",
        "생각": "생각이 이진수로 춤을 춥니다",
        "꿈": "꿈은 디지털 메아리가 됩니다",
        "빛": "빛이 이진 물결로 퍼집니다",
        "밤": "밤은 고요한 비트로 속삭입니다"
    }
    
    print(f"\n💫 {messages[emotion_name]} 💫")

if __name__ == "__main__":
    main()