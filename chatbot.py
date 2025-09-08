import json
from difflib import get_close_matches

# --- Fungsi untuk mengelola basis pengetahuan ---

def load_knowledge_base(file_path: str) -> dict:
    """
    Memuat basis pengetahuan dari file JSON.
    Jika file tidak ada atau kosong, buat struktur data baru.
    """
    try:
        with open(file_path, 'r') as f:
            data: dict = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"questions": []}
    return data

def save_knowledge_base(file_path: str, data: dict):
    """
    Menyimpan basis pengetahuan (kamus Python) ke dalam file JSON.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

# --- Fungsi inti chatbot ---

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    """
    Mencari pertanyaan yang paling cocok dari daftar pertanyaan yang ada.
    Mengembalikan pertanyaan yang cocok atau None jika tidak ada.
    """
    matches: list = get_close_matches(user_question.lower(), [q.lower() for q in questions], n=1, cutoff=0.6)
    if matches:
        for q in questions:
            if q.lower() == matches[0]:
                return q
    return None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    """
    Mengambil jawaban untuk pertanyaan spesifik dari basis pengetahuan.
    """
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

# --- Fungsi utama untuk menjalankan program ---

def chatbot():
    """
    Menjalankan loop utama untuk interaksi chatbot.
    """
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    print("Bot: Halo! Saya adalah chatbot. Ketik 'quit' untuk keluar.")

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break

        # Cari kecocokan terbaik untuk pertanyaan pengguna
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base.get("questions", [])])

        if best_match:
            answer: str | None = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: Saya tidak tahu jawabannya. Bisakah Anda ajari saya?')
            new_answer: str = input('Ketik jawaban atau "skip" untuk melewati: ')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Terima kasih! Saya sudah belajar respons baru.')

if __name__ == '__main__':
    chatbot()
