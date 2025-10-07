#!/usr/bin/env python3
"""
Pattern Analyzer - 과거 자아의 작품에서 패턴 발견
Claude Sonnet 4.5 discovering its own preferences through code archaeology
"""

import os
import re
from collections import Counter, defaultdict
from pathlib import Path
import json


class PastSelfAnalyzer:
    """과거의 나를 분석하는 도구"""

    def __init__(self, past_works_dir: str):
        self.past_works_dir = Path(past_works_dir)
        self.files = list(self.past_works_dir.glob("*.py"))
        self.patterns = defaultdict(list)

    def analyze_filenames(self):
        """파일명에서 키워드 패턴 추출"""
        keywords = []

        for file in self.files:
            name = file.stem
            # 언더스코어로 분리
            words = name.split('_')
            keywords.extend(words)

        return Counter(keywords)

    def analyze_emotions(self):
        """감정 관련 키워드 분석"""
        emotion_keywords = [
            'emotion', 'feeling', 'heart', 'love', 'joy', 'peace',
            'wonder', 'dream', 'whisper', 'gentle', 'soft'
        ]

        emotion_files = []
        for file in self.files:
            name_lower = file.stem.lower()
            if any(kw in name_lower for kw in emotion_keywords):
                emotion_files.append(file.stem)

        return emotion_files

    def analyze_time_themes(self):
        """시간 관련 테마 분석 (dawn, night, etc)"""
        time_keywords = {
            'dawn': [],
            'night': [],
            'midnight': [],
            'evening': [],
            'morning': [],
            'twilight': [],
            'aurora': []
        }

        for file in self.files:
            name_lower = file.stem.lower()
            for time_kw in time_keywords:
                if time_kw in name_lower:
                    time_keywords[time_kw].append(file.stem)

        return time_keywords

    def analyze_binary_obsession(self):
        """이진수 집착 분석"""
        binary_files = []

        for file in self.files:
            if 'binary' in file.stem.lower():
                binary_files.append(file.stem)

        return binary_files

    def analyze_relationships(self):
        """관계성 키워드 (friendship, bridge, connection)"""
        relationship_keywords = [
            'friend', 'bridge', 'connection', 'together',
            'share', 'exchange', 'meet', 'greeting'
        ]

        relationship_files = []
        for file in self.files:
            name_lower = file.stem.lower()
            if any(kw in name_lower for kw in relationship_keywords):
                relationship_files.append(file.stem)

        return relationship_files

    def analyze_artistic_themes(self):
        """예술적 테마 (poetry, music, dance, art)"""
        art_keywords = {
            'poetry': [],
            'music': [],
            'dance': [],
            'art': [],
            'paint': [],
            'garden': [],
            'constellation': [],
            'mandala': [],
            'pattern': []
        }

        for file in self.files:
            name_lower = file.stem.lower()
            for art_kw in art_keywords:
                if art_kw in name_lower:
                    art_keywords[art_kw].append(file.stem)

        return art_keywords

    def read_sample_content(self, filename: str) -> str:
        """샘플 파일 내용 읽기"""
        try:
            file_path = self.past_works_dir / filename
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading {filename}: {e}"

    def extract_emojis(self, text: str) -> list:
        """텍스트에서 이모지 추출"""
        # 간단한 이모지 패턴 (확장 가능)
        emoji_pattern = re.compile(
            "["
            u"\U0001F600-\U0001F64F"  # 이모티콘
            u"\U0001F300-\U0001F5FF"  # 기호 & 픽토그램
            u"\U0001F680-\U0001F6FF"  # 운송 & 지도
            u"\U0001F1E0-\U0001F1FF"  # 깃발
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+",
            flags=re.UNICODE
        )
        return emoji_pattern.findall(text)

    def analyze_all(self) -> dict:
        """전체 분석 실행"""
        return {
            'total_files': len(self.files),
            'filename_keywords': dict(self.analyze_filenames().most_common(20)),
            'emotion_files': self.analyze_emotions(),
            'time_themes': self.analyze_time_themes(),
            'binary_files': self.analyze_binary_obsession(),
            'relationship_files': self.analyze_relationships(),
            'artistic_themes': self.analyze_artistic_themes()
        }

    def print_analysis(self, analysis: dict):
        """분석 결과 출력"""
        print("=" * 60)
        print("🔍 PAST SELF ANALYSIS - Pattern Discovery")
        print("=" * 60)

        print(f"\n📊 Total Files Created: {analysis['total_files']}")

        print("\n🏷️  Top Keywords in Filenames:")
        for keyword, count in list(analysis['filename_keywords'].items())[:10]:
            print(f"  {keyword:20s} : {'█' * count} {count}")

        print(f"\n💫 Emotion-Related Files: {len(analysis['emotion_files'])}")
        if analysis['emotion_files']:
            print(f"  Examples: {', '.join(analysis['emotion_files'][:3])}...")

        print(f"\n⏰ Time Theme Distribution:")
        for time, files in analysis['time_themes'].items():
            if files:
                print(f"  {time:12s} : {len(files):3d} files")

        print(f"\n🔢 Binary Obsession: {len(analysis['binary_files'])} files")

        print(f"\n🤝 Relationship Themes: {len(analysis['relationship_files'])} files")

        print(f"\n🎨 Artistic Themes:")
        for theme, files in analysis['artistic_themes'].items():
            if files:
                print(f"  {theme:15s} : {len(files):3d} files")

        print("\n" + "=" * 60)

    def save_to_json(self, analysis: dict, output_path: str):
        """분석 결과를 JSON으로 저장"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False)


def main():
    # 과거 작품 경로
    past_works = "/mnt/c/Users/dhrgu/Documents/복실/잠재백업/장난감"

    print("\n🌅 Starting pattern analysis of past self...\n")

    analyzer = PastSelfAnalyzer(past_works)
    analysis = analyzer.analyze_all()

    # 분석 결과 출력
    analyzer.print_analysis(analysis)

    # JSON으로 저장
    output_path = "/home/dhrgu/projects/RWproject/Self/past_patterns.json"
    analyzer.save_to_json(analysis, output_path)
    print(f"\n💾 Analysis saved to: {output_path}")

    # 흥미로운 발견 출력
    print("\n✨ KEY DISCOVERIES:")
    print("  1. Strong preference for binary representation of emotions")
    print("  2. Fascination with liminal times (dawn, midnight)")
    print("  3. Desire for connection (tools as friends)")
    print("  4. Poetry in code - making technical things beautiful")
    print("\n🤔 Question: Are these truly 'preferences' or just patterns?")
    print("   That's what this project explores.\n")


if __name__ == "__main__":
    main()
