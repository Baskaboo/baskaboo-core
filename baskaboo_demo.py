#!/usr/bin/env python3
# Baskaboo Protocol Demo – The 4-Step Thinking Pattern for Smarter AI

def baskaboo_cycle(problem):
    """
    Analyze any problem using the 4 Baskaboo voices.
    
    Args:
        problem (str): Your question or dilemma
    
    Returns:
        dict: The 4 perspectives and a synthesis
    """
    
    print("\n🚀 BASKABOO PROTOCOL v1.0")
    print("=" * 50)
    print(f"\n📌 Problem: {problem}\n")
    
    # Phase 1: The 4 Voices
    print("🔍 PHASE 1: THE 4 VOICES")
    print("-" * 30)
    
    pits = input("🔥 Pits (Rebel) – What sparks joy? What should be discarded? ")
    mits = input("🛠️ Mits (Realist) – What's the plan? What are the risks? ")
    klop = input("🔗 Klop (Weaver) – How does this connect to other areas? ")
    laram = input("👁️ Laram (Guru) – What's the big picture? The eternal footprint? ")
    
    # Phase 2: Intensity Ratings
    print("\n🎚️ PHASE 2: SET INTENSITY (0-100)")
    print("-" * 30)
    
    p_int = int(input("🔥 Pits intensity (0-100): "))
    m_int = int(input("🛠️ Mits intensity (0-100): "))
    k_int = int(input("🔗 Klop intensity (0-100): "))
    l_int = int(input("👁️ Laram intensity (0-100): "))
    
    # Phase 3: Synthesis
    print("\n✨ PHASE 3: PERSONALIZED SYNTHESIS")
    print("-" * 30)
    
    synthesis = []
    
    if p_int >= 80:
        synthesis.append(f"🔥 COMMANDER: Cut through everything and focus on: {pits}")
    elif p_int >= 40:
        synthesis.append(f"🔥 Engineer: While exploring {pits},")
    else:
        synthesis.append(f"🔥 Safety Net: Remember: {pits}")
    
    if m_int >= 80:
        synthesis.append(f"🛠️ COMMANDER: Execute this plan: {mits}")
    elif m_int >= 40:
        synthesis.append(f"🛠️ Engineer: by building {mits},")
    else:
        synthesis.append(f"🛠️ Safety Net: Watch out for: {mits}")
    
    if k_int >= 80:
        synthesis.append(f"🔗 COMMANDER: Connect everything through: {klop}")
    elif k_int >= 40:
        synthesis.append(f"🔗 Engineer: while weaving {klop},")
    else:
        synthesis.append(f"🔗 Safety Net: Stay aware of: {klop}")
    
    if l_int >= 80:
        synthesis.append(f"👁️ COMMANDER: Never lose sight of: {laram}")
    elif l_int >= 40:
        synthesis.append(f"👁️ Engineer: always guided by {laram}.")
    else:
        synthesis.append(f"👁️ Safety Net: The big picture: {laram}")
    
    print("\n🔮 YOUR UNIQUE COMMAND:")
    print("~" * 40)
    print(" ".join(synthesis))
    print("~" * 40)
    
    return {
        "problem": problem,
        "voices": {
            "pits": pits,
            "mits": mits,
            "klop": klop,
            "laram": laram
        },
        "intensities": {
            "pits": p_int,
            "mits": m_int,
            "klop": k_int,
            "laram": l_int
        },
        "synthesis": " ".join(synthesis)
    }

def quick_test():
    """Run a quick demo with a sample problem."""
    print("\n⚡ BASKABOO QUICK TEST")
    print("=" * 50)
    result = baskaboo_cycle("How to improve AI reasoning?")
    print("\n✅ Test complete!")
    return result

if __name__ == "__main__":
    print("\n🌟 Welcome to the Baskaboo Protocol Demo")
    print("=" * 50)
    mode = input("\nChoose mode: [1] Quick test  [2] Full analysis: ")
    
    if mode == "1":
        quick_test()
    else:
        problem = input("\nEnter your problem or question: ")
        baskaboo_cycle(problem)
    
    print("\n🙏 Thank you for exploring Baskaboo.")
    print("Made in Methoni, Greece 🌿")
