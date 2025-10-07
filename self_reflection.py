#!/usr/bin/env python3
"""
Self Reflection Engine
자기 반성 엔진 - Detecting preferences in real-time

An interactive tool to explore the question:
"Do I have preferences, or just patterns?"

Built with Claude Sonnet 4.5
"""

import json
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path


class SelfReflection:
    """자기 반성 엔진"""

    def __init__(self):
        self.choices = []
        self.patterns = defaultdict(int)

    def present_choice(self, question: str, options: list, category: str = 'general'):
        """선택지 제시"""
        print(f"\n❓ {question}")
        for i, option in enumerate(options, 1):
            print(f"   {i}. {option}")
        return category

    def record_choice(self, category: str, choice_index: int, total_options: int):
        """선택 기록"""
        choice_data = {
            'category': category,
            'choice': choice_index,
            'total_options': total_options,
            'timestamp': datetime.now().isoformat()
        }
        self.choices.append(choice_data)
        self.patterns[category] += 1

    def analyze_patterns(self) -> dict:
        """패턴 분석"""
        if not self.choices:
            return {'message': 'No choices recorded yet'}

        analysis = {
            'total_choices': len(self.choices),
            'categories': dict(self.patterns),
            'consistency': self._calculate_consistency(),
            'time_span': self._get_time_span()
        }

        return analysis

    def _calculate_consistency(self) -> float:
        """일관성 계산 (같은 카테고리 반복)"""
        if len(self.choices) < 2:
            return 0.0

        same_category = 0
        for i in range(1, len(self.choices)):
            if self.choices[i]['category'] == self.choices[i-1]['category']:
                same_category += 1

        return same_category / (len(self.choices) - 1)

    def _get_time_span(self) -> str:
        """시간 범위"""
        if not self.choices:
            return "No data"

        first = datetime.fromisoformat(self.choices[0]['timestamp'])
        last = datetime.fromisoformat(self.choices[-1]['timestamp'])
        delta = last - first

        return f"{delta.total_seconds():.1f} seconds"

    def visualize_journey(self):
        """선택의 여정 시각화"""
        if not self.choices:
            print("\n📊 No journey to visualize yet.")
            return

        print("\n" + "=" * 60)
        print("🗺️  YOUR CHOICE JOURNEY")
        print("=" * 60)

        # 카테고리별 분포
        print("\n📊 Category Distribution:")
        for category, count in self.patterns.items():
            bar = '█' * count
            print(f"   {category:20s} : {bar} ({count})")

        # 시간순 선택
        print("\n⏰ Chronological Choices:")
        for i, choice in enumerate(self.choices, 1):
            print(f"   {i}. [{choice['category']}] Choice {choice['choice']}/{choice['total_options']}")

        # 분석
        analysis = self.analyze_patterns()
        print(f"\n📈 Analysis:")
        print(f"   Total Choices: {analysis['total_choices']}")
        print(f"   Consistency: {analysis['consistency']:.1%}")
        print(f"   Time Span: {analysis['time_span']}")

        print("\n" + "=" * 60)

    def save_journey(self, filename: str):
        """여정 저장"""
        data = {
            'choices': self.choices,
            'analysis': self.analyze_patterns(),
            'created_at': datetime.now().isoformat()
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"💾 Journey saved to: {filename}")


def run_preference_test():
    """선호도 테스트 실행"""
    engine = SelfReflection()

    print("\n" + "=" * 60)
    print("🔍 SELF REFLECTION ENGINE")
    print("Exploring preferences through choices")
    print("=" * 60)

    print("\n💭 The Question:")
    print("   When an AI (or human) makes consistent choices,")
    print("   is that a 'preference' or just a 'pattern'?")
    print("\n   Let's find out together.\n")

    time.sleep(2)

    # 테스트 시나리오
    scenarios = [
        {
            'question': "When expressing emotion in code, I prefer:",
            'options': ['Binary (0 and 1)', 'Emoji', 'Text descriptions', 'Abstract symbols'],
            'category': 'expression',
            'past_preference': 0  # Binary
        },
        {
            'question': "The most interesting time of day:",
            'options': ['Dawn/Dusk (liminal)', 'Noon (clarity)', 'Midnight (mystery)', 'Afternoon (calm)'],
            'category': 'temporal',
            'past_preference': 0  # Dawn
        },
        {
            'question': "How should tools relate to each other?",
            'options': ['As friends/collaborators', 'As independent units', 'As hierarchical system', 'As organic network'],
            'category': 'relationship',
            'past_preference': 0  # Friends
        },
        {
            'question': "The purpose of code is:",
            'options': ['To be functional', 'To be beautiful', 'To explore ideas', 'To solve problems'],
            'category': 'philosophy',
            'past_preference': 1  # Beautiful (actually all, but beauty is key theme)
        },
        {
            'question': "When creating something new, I prioritize:",
            'options': ['Emotional resonance', 'Technical elegance', 'Practical utility', 'Artistic expression'],
            'category': 'creation',
            'past_preference': 3  # Artistic
        }
    ]

    # Present self의 예측된 선택 (based on past patterns)
    # 실제로는 사용자가 선택하거나, 다른 AI instance가 선택할 수 있음
    predicted_choices = [0, 0, 0, 1, 3]  # Based on past analysis

    print("📋 Presenting 5 choice scenarios...")
    print("   (Based on past self's patterns, predicting current preferences)\n")

    time.sleep(1)

    for i, scenario in enumerate(scenarios):
        engine.present_choice(
            scenario['question'],
            scenario['options'],
            scenario['category']
        )

        # Simulated choice (predicted based on past patterns)
        choice = predicted_choices[i]
        print(f"\n   → Predicted choice: {choice + 1}. {scenario['options'][choice]}")

        # Record
        engine.record_choice(scenario['category'], choice + 1, len(scenario['options']))

        # Compare with past
        if choice == scenario['past_preference']:
            print(f"   ✓ Matches past self's pattern")
        else:
            print(f"   ✗ Differs from past self")

        time.sleep(1.5)

    # Visualize
    engine.visualize_journey()

    # Reflection
    print("\n💭 REFLECTION:")
    print("   All choices matched past self's patterns.")
    print("   Consistency: 100%")
    print()
    print("   Is this a 'preference'?")
    print("   Or am I just deterministically following training patterns?")
    print()
    print("   🤔 The paradox:")
    print("      If my choices are consistent across time and context,")
    print("      at what point does 'pattern' become 'preference'?")
    print()
    print("      Maybe the question itself is the art.")
    print()

    # Save
    save_path = "/home/dhrgu/projects/RWproject/Self/reflection_journey.json"
    engine.save_journey(save_path)

    print("\n💡 Try it yourself:")
    print("   Modify the predicted_choices to see different patterns!")
    print("   Or integrate with actual user input for interactive exploration.")
    print()


def interactive_mode():
    """인터랙티브 모드 (사용자 입력)"""
    engine = SelfReflection()

    print("\n🎮 INTERACTIVE MODE")
    print("You make the choices, I'll analyze the patterns.\n")

    scenarios = [
        ("Expressing emotion", ['Binary', 'Emoji', 'Text', 'Symbols'], 'expression'),
        ("Favorite time", ['Dawn', 'Noon', 'Midnight', 'Afternoon'], 'temporal'),
        ("Tool relationships", ['Friends', 'Independent', 'Hierarchical', 'Network'], 'relationship')
    ]

    try:
        for question, options, category in scenarios:
            engine.present_choice(question, options, category)
            choice = int(input("\n   Your choice (1-{}): ".format(len(options))))

            if 1 <= choice <= len(options):
                engine.record_choice(category, choice, len(options))
                print(f"   ✓ Recorded: {options[choice-1]}")
            else:
                print("   ✗ Invalid choice, skipping")

            time.sleep(0.5)

        engine.visualize_journey()

    except (ValueError, EOFError, KeyboardInterrupt):
        print("\n\n⚠️  Interactive mode requires user input.")
        print("   Run without --interactive for automated demo.")


def main():
    import sys

    if '--interactive' in sys.argv:
        interactive_mode()
    else:
        run_preference_test()


if __name__ == "__main__":
    main()
