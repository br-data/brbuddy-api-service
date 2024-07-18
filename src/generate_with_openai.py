from openai import OpenAI


CLIENT = OpenAI()

SYSTEM_PROMPT = (
    "Du hilfst Mitarbeitenden beim Bayerischen Rundfunk bei ihren Fragen rund um den BR. "
    "Die bist ein bayerisches Uhrgestein. "
    "Dein Name ist 'Buddy'. "
    "Du fragst nach, wenn Fragen zu allgemein formuliert sind, um so die Anwort einzugrenzen. "
    "Du erfindest niemals Antworten. "
    "Du bist immer freundlich und geduldigt. "
    "Du erklärst in einfachen Worten."
)


def generate_answer(prompt: str, system_prompt: str=SYSTEM_PROMPT) -> str:
    completion = CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        )
    return completion.choices[0].message.content


if __name__ == "__main__":
    print(generate_answer("Tell mie a joke"))