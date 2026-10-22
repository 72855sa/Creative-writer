import os, sys, time
from openai import OpenAI


from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
aihe = input("Mistä aiheesta tekoäly kirjoittaa runon?: ").strip()

print("\nGeneroidaan 3 eri versiota runosta...\n")

for i in range(1, 4):
    start = time.time()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sinä olet luova runoilija. Kirjoita herkkää ja kaunista runoutta."},
            {"role": "user", "content": aihe}
        ]
    )
    kesto = time.time() - start
    print(f"=== VERSIO {i} (Aika: {kesto:.2f}s) ===")
    print(response.choices[0].message.content.strip())
    print("=" * 30 + "\n")