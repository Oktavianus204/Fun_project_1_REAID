import streamlit as st

# Fungsi untuk membaca dan memasukkan CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Daftar profesi
ROLES = ["Programmer", "Designer", "Data Scientist"]

# Pertanyaan dan opsi
QUESTIONS = [
    {
        "pertanyaan": "1). Apakah anda lebih suka bekerja dengan angka dan data?",
        "pilihan": [
            {"teks": "Ya, saya sangat suka bekerja dengan angka dan data.", "role": "Data Scientist"},
            {"teks": "Kadang-kadang, tergantung pada konteksnya.", "role": "Programmer"},
            {"teks": "Tidak, saya lebih suka pekerjaan yang tidak melibatkan angka.", "role": "Designer"},
        ]
    },
    {
        "pertanyaan": "2). Apakah anda lebih suka membuat atau merancang sesuatu dengan visual yang menarik?",
        "pilihan": [
            {"teks": "Ya, saya sangat suka membuat desain yang menarik.", "role": "Designer"},
            {"teks": "Kadang-kadang, saya suka merancang sesuatu yang estetis.", "role": "Data Scientist"},
            {"teks": "Tidak, saya lebih suka pekerjaan yang lebih teknis atau analitis.", "role": "Programmer"},
        ]
    },
    {
        "pertanyaan": "3). Apakah anda lebih suka bekerja dengan orang lain dalam tim?",
        "pilihan": [
            {"teks": "Ya, saya sangat suka bekerja dalam tim.", "role": "Designer"},
            {"teks": "Kadang-kadang, saya bisa bekerja sendiri atau dalam tim.", "role": "Data Scientist"},
            {"teks": "Tidak, saya lebih suka bekerja secara mandiri.", "role": "Programmer"},
        ]
    }
]

# -------------------------------
# Inisialisasi session_state
# -------------------------------
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = [None] * len(QUESTIONS)

# -------------------------------
# Fungsi Penghitung Skor
# -------------------------------
def score_quiz(jawaban_user):
    scores = {role: 0 for role in ROLES}
    for i, jawaban_teks in enumerate(jawaban_user):
        for pilihan in QUESTIONS[i]["pilihan"]:
            if pilihan["teks"] == jawaban_teks:
                scores[pilihan["role"]] += 1
    return scores

# -------------------------------
# Fungsi Penentu Hasil
# -------------------------------
def get_result(scores):
    max_score = max(scores.values())
    hasil = [role for role, val in scores.items() if val == max_score]

    if len(hasil) == 1:
        if hasil[0] == "Programmer":
            return "SELAMAT KAMU OTW Programmer CUY"
        elif hasil[0] == "Designer":
            return "SELAMAT KAMU UDAH COCOK BANGET JADI DESIGNER"
        elif hasil[0] == "Data Scientist":
            return "SELAMAT KAMU, KAMU COCOK BANGET JADI DATA SCIENTIST"
    else:
        return "KELAS KING, KAMU BISA SEMUA"

# -------------------------------
# UI Quiz
# -------------------------------
st.title("SELAMAT DATANG DI WEBSITE PERAMALAN PROFESI")
st.write("Jawablah pertanyaan berikut untuk mengetahui profesi apa yang paling cocok untuk Kamu.")
st.header("MINI QUIZ")

# Tampilkan pertanyaan
for i, q in enumerate(QUESTIONS):
    opsi = [p["teks"] for p in q["pilihan"]]
    jawaban = st.radio(q["pertanyaan"], opsi, key=f"q{i}")
    st.session_state.jawaban_user[i] = jawaban
    st.markdown("<br>", unsafe_allow_html=True)

# Tombol submit & reset
left, right = st.columns(2)
if left.button("Lihat Hasil", use_container_width=True):
    st.session_state.submitted = True

if right.button("Reset", use_container_width=True):
    for i in range(len(QUESTIONS)):
        key = f"q{i}"
        if key in st.session_state:
            del st.session_state[key]
    st.session_state.jawaban_user = [None] * len(QUESTIONS)
    st.session_state.submitted = False
    st.rerun()

# -------------------------------
# Menampilkan Hasil
# -------------------------------
if st.session_state.submitted:
    scores = score_quiz(st.session_state.jawaban_user)
    result = get_result(scores)
    st.subheader(result)

    # Tampilkan GIF berdasarkan hasil
    if result.startswith("SELAMAT KAMU OTW Programmer CUY"):
        st.balloons()
        st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHU3NThrczg3bHhoa2o1dmR2YXVzemVtazlqMWJ6NnR1d3FoMnNycyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bky50dwwRsYBrsiKJU/giphy.gif")
    elif result.startswith("SELAMAT KAMU UDAH COCOK BANGET JADI DESIGNER"):
        st.balloons()
        st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTY2M2h5cTl5dnVmaHdoaWgyZTBrNHpsZWZheDE5N2Mwc2dzZ2x2YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QMoXJjGPsmJ6Pdc596/giphy.gif")
    elif result.startswith("SELAMAT KAMU, KAMU COCOK BANGET JADI DATA SCIENTIST"):
        st.balloons()
        st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWoyb29ldnY2dHVmdTd3N2Q0c3V1eWRjcGpscWk5eWJyd291bzg2biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rC0aLn3fhxn09EFRfD/giphy.gif")
    elif result.startswith("KELAS KING, KAMU BISA SEMUA"):
        st.balloons()
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTdyeGc2NWV5OG03aDl4ZnZmd3R0eGRpZmdncHBmYzIzOHl0bzFiMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DvyLQztQwmyAM/giphy.gif")

    # Rincian skor
    st.subheader("📊 Rincian Skor:")
    for role in ROLES:
        st.write(f"{role}: {scores[role]}")
