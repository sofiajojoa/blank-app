```python
import random

import streamlit as st


st.set_page_config(
    page_title="Aprendamos Juntos",
    page_icon="🦉",
    layout="wide",
    initial_sidebar_state="expanded",
)


READING_CHALLENGES = {
    1: [
        {"emoji": "🐱", "pattern": "G_TO", "answer": "A", "hint": "Un animal que dice miau"},
        {"emoji": "🐥", "pattern": "POLL_TO", "answer": "I", "hint": "Un pollito pequeño"},
        {"emoji": "🌙", "pattern": "L_NA", "answer": "U", "hint": "Brilla en el cielo de noche"},
        {"emoji": "🍇", "pattern": "UV_S", "answer": "A", "hint": "Fruta pequeña que crece en racimos"},
    ],
    2: [
        {"emoji": "🪑", "pattern": "S_LLA", "answer": "I", "hint": "Nos sentamos en ella"},
        {"emoji": "🐶", "pattern": "PERR_", "answer": "O", "hint": "Un amigo peludo que ladra"},
        {"emoji": "☀️", "pattern": "S_L", "answer": "O", "hint": "Calienta e ilumina el día"},
        {"emoji": "🍋", "pattern": "L_MÓN", "answer": "I", "hint": "Fruta amarilla y un poquito ácida"},
    ],
    3: [
        {"emoji": "❤️", "pattern": "C_RAZÓN", "answer": "O", "hint": "Late dentro de nuestro pecho"},
        {"emoji": "⭐", "pattern": "ESTR_LLA", "answer": "E", "hint": "Brilla en el cielo"},
        {"emoji": "🎵", "pattern": "MÚS_CA", "answer": "I", "hint": "La escuchamos y podemos cantarla"},
        {"emoji": "🦋", "pattern": "M_RIPOSA", "answer": "A", "hint": "Insecto de alas coloridas"},
    ],
}

MATH_CHALLENGES = {
    1: [
        {"kind": "count", "emoji": "🍓", "count": 4, "label": "fresas"},
        {"kind": "add", "left": 2, "right": 3},
        {"kind": "count", "emoji": "⭐", "count": 6, "label": "estrellas"},
        {"kind": "add", "left": 4, "right": 3},
    ],
    2: [
        {"kind": "count", "emoji": "🍊", "count": 8, "label": "naranjas"},
        {"kind": "add", "left": 6, "right": 5},
        {"kind": "count", "emoji": "🐠", "count": 9, "label": "pececitos"},
        {"kind": "add", "left": 8, "right": 7},
    ],
    3: [
        {"kind": "count", "emoji": "🍎", "count": 12, "label": "manzanas"},
        {"kind": "add", "left": 12, "right": 7},
        {"kind": "count", "emoji": "🔷", "count": 14, "label": "figuras"},
        {"kind": "add", "left": 16, "right": 8},
    ],
}


def submit_answer(challenge_id, selected, answer):
    if challenge_id in st.session_state.solved_challenges:
        return
    if selected == answer:
        st.session_state.solved_challenges.add(challenge_id)
        st.session_state.points += 10
        st.session_state.last_try = None
        st.session_state.celebration_for = challenge_id
    else:
        st.session_state.last_try = challenge_id


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@500;600;700;800;900&display=swap');

    :root {
      --ink: #25365b;
      --purple: #6c63d9;
      --mint: #dff8ed;
      --peach: #fff0dd;
    }
    html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
    .stApp {
      background:
        radial-gradient(ellipse at 7% 5%, rgba(255, 220, 166, .48), transparent 28%),
        radial-gradient(ellipse at 94% 22%, rgba(199, 232, 255, .58), transparent 28%),
        linear-gradient(140deg, #fffaf0 0%, #f5f5ff 53%, #effcf7 100%);
      color: var(--ink);
    }
    header[data-testid="stHeader"] { display: none; }
    [data-testid="stMainBlockContainer"] { max-width: 1120px; padding-top: 2rem; padding-bottom: 3rem; }
    [data-testid="stSidebar"] {
      background: linear-gradient(180deg, #fff3d9 0%, #f9efff 55%, #edf9ff 100%);
      border-right: 1px solid rgba(108, 99, 217, .12);
    }
    [data-testid="stSidebar"] > div:first-child { padding-top: 1.2rem; }
    h1, h2, h3, p, label { color: var(--ink); }
    .brand-mark { color: #7568d9; font-size: .9rem; font-weight: 900; letter-spacing: .12em; text-transform: uppercase; }
    .page-title { color: #26345a; font-size: clamp(2.1rem, 5vw, 3.1rem); font-weight: 900; line-height: 1.04; margin: .15rem 0 .45rem; }
    .page-subtitle { color: #64708f; font-size: 1.08rem; margin-bottom: 1.5rem; }
    .welcome-card {
      display: flex; align-items: center; gap: 1.15rem;
      background: linear-gradient(110deg, #fff 0%, #fff8e9 100%);
      border: 2px solid #f5dfae; border-radius: 26px; padding: 1.25rem 1.45rem;
      box-shadow: 0 10px 26px rgba(95, 80, 140, .08); margin: .35rem 0 1.3rem;
    }
    .owl-avatar {
      flex: 0 0 82px; width: 82px; height: 82px; border-radius: 25px;
      display: grid; place-items: center; font-size: 3.6rem;
      background: linear-gradient(145deg, #f3e6ff, #dcecff);
    }
    .welcome-title { font-weight: 900; font-size: 1.28rem; color: #4e479c; margin-bottom: .16rem; }
    .welcome-copy { color: #586484; font-size: 1rem; line-height: 1.5; }
    .stat-card {
      border-radius: 20px; padding: .85rem 1rem; min-height: 88px;
      background: rgba(255,255,255,.82); border: 1px solid rgba(108,99,217,.13);
    }
    .stat-label { color: #71809a; font-weight: 800; font-size: .82rem; text-transform: uppercase; letter-spacing: .06em; }
    .stat-value { color: #5b50c9; font-size: 1.55rem; font-weight: 900; margin-top: .1rem; }
    .challenge-kicker { color: #7770cf; text-transform: uppercase; letter-spacing: .1em; font-size: .8rem; font-weight: 900; }
    .challenge-title { color: #2b385e; font-size: 1.62rem; font-weight: 900; margin: .1rem 0 .25rem; }
    .challenge-copy { color: #6b7691; font-size: 1rem; }
    .word-display {
      display: flex; justify-content: center; align-items: center; gap: .08em;
      margin: 1.1rem 0 .45rem; color: #394773; font-weight: 900;
      font-size: clamp(2.5rem, 7vw, 4.2rem); letter-spacing: .06em;
    }
    .missing-letter {
      color: #ef8e42; background: #fff0d9; border: 3px dashed #f4b66b;
      min-width: .82em; height: 1.08em; display: inline-flex; justify-content: center; align-items: center;
      border-radius: 15px; margin: 0 .05em;
    }
    .picture-emoji { text-align: center; font-size: 3.7rem; margin: .15rem 0; }
    .hint-pill {
      text-align: center; color: #6e7391; background: #f3f0ff;
      border-radius: 999px; padding: .45rem .85rem; font-weight: 700; margin: .4rem auto 1rem;
      width: fit-content;
    }
    .objects-board {
      display: flex; flex-wrap: wrap; justify-content: center; gap: .48rem;
      padding: 1.1rem; margin: .8rem auto 1rem; max-width: 620px;
      background: linear-gradient(135deg, #effaff, #f7f2ff);
      border: 2px solid #e1e5fa; border-radius: 24px;
    }
    .count-object {
      width: 62px; height: 62px; display: grid; place-items: center;
      background: white; border-radius: 19px; font-size: 2.15rem;
      box-shadow: 0 4px 10px rgba(72, 93, 144, .09);
    }
    .sum-display {
      display: flex; justify-content: center; align-items: center; gap: 1rem;
      margin: 1.25rem 0; color: #394773; font-size: clamp(2.7rem, 8vw, 4.5rem); font-weight: 900;
    }
    .sum-number { background: #fff4dc; padding: .12rem .62rem; border-radius: 20px; }
    .sum-plus { color: #ee9b43; }
    .stButton > button {
      min-height: 58px; border-radius: 18px; border: 2px solid #e4e4f6;
      color: #39436d; background: #fff; font-family: 'Nunito', sans-serif;
      font-size: 1.13rem; font-weight: 900; box-shadow: 0 5px 0 rgba(93, 92, 160, .11);
      transition: transform .14s ease, box-shadow .14s ease, border-color .14s ease;
    }
    .stButton > button:hover:not(:disabled) {
      transform: translateY(-2px); border-color: #aaa2f1; color: #5148bc;
      box-shadow: 0 7px 0 rgba(93, 92, 160, .12);
    }
    div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(1) .stButton > button { background: #fff1d8; border-color: #f5d596; }
    div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(2) .stButton > button { background: #e5f6ff; border-color: #bfdef2; }
    div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(3) .stButton > button { background: #eee9ff; border-color: #d3c9f7; }
    div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(4) .stButton > button { background: #e3f8ee; border-color: #bbe7d0; }
    div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(5) .stButton > button { background: #ffe9ef; border-color: #f1c5d2; }
    .stButton > button:disabled { opacity: .65; }
    .stAlert { border-radius: 18px; font-weight: 800; }
    [data-testid="stRadio"] label, [data-testid="stSelectbox"] label { font-weight: 900; color: #4a4b78; }
    [data-testid="stRadio"] [role="radiogroup"] label {
      background: rgba(255,255,255,.72); padding: .55rem .65rem; margin: .2rem 0;
      border-radius: 14px; border: 1px solid rgba(108,99,217,.1);
    }
    .sidebar-note { color: #707a98; font-size: .9rem; line-height: 1.45; margin-top: 1.2rem; }
    @media (max-width: 640px) {
      [data-testid="stMainBlockContainer"] { padding: 1.1rem 1rem 2rem; }
      .welcome-card { align-items: flex-start; padding: 1rem; }
      .owl-avatar { flex-basis: 64px; width: 64px; height: 64px; font-size: 2.8rem; border-radius: 20px; }
      .count-object { width: 48px; height: 48px; font-size: 1.8rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


if "points" not in st.session_state:
    st.session_state.points = 0
if "activity_index" not in st.session_state:
    st.session_state.activity_index = 0
if "solved_challenges" not in st.session_state:
    st.session_state.solved_challenges = set()
if "last_try" not in st.session_state:
    st.session_state.last_try = None
if "celebration_for" not in st.session_state:
    st.session_state.celebration_for = None


with st.sidebar:
    st.markdown('<div style="font-size:3.3rem; text-align:center;">🦉</div>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align:center; font-size:1.28rem; font-weight:900; color:#514a9c; margin-bottom:1.2rem;">¡Hola, explorador!</div>',
        unsafe_allow_html=True,
    )
    grade = st.selectbox(
        "Elige tu grado",
        options=[1, 2, 3],
        format_func=lambda value: f"{value}.º de primaria",
    )
    subject = st.radio("¿Qué vamos a aprender?", ["Lectura", "Matemáticas"])
    st.markdown(
        '<div class="sidebar-note">Cada reto es una oportunidad para aprender. ¡Tú puedes!</div>',
        unsafe_allow_html=True,
    )


st.markdown('<div class="brand-mark">Tu aventura de aprendizaje</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">Aprendamos Juntos</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="page-subtitle">Un reto divertido de {subject.lower()} para {grade}.º de primaria.</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="welcome-card">
      <div class="owl-avatar">🦉</div>
      <div>
        <div class="welcome-title">¡Hola! Soy Búho Sabio</div>
        <div class="welcome-copy">Me alegra aprender contigo. ¡Vamos paso a paso y celebremos cada logro!</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

stat_left, stat_right = st.columns([1, 2])
with stat_left:
    st.markdown(
        f'<div class="stat-card"><div class="stat-label">⭐ Mis puntos</div><div class="stat-value">{st.session_state.points}</div></div>',
        unsafe_allow_html=True,
    )
with stat_right:
    st.markdown(
        f'<div class="stat-card"><div class="stat-label">📚 Mi aventura</div><div class="stat-value">{subject} · {grade}.º</div></div>',
        unsafe_allow_html=True,
    )

st.write("")
challenge_list = READING_CHALLENGES[grade] if subject == "Lectura" else MATH_CHALLENGES[grade]
challenge_number = st.session_state.activity_index % len(challenge_list)
challenge_id = f"{grade}-{subject}-{st.session_state.activity_index}"
challenge = challenge_list[challenge_number]
solved = challenge_id in st.session_state.solved_challenges
if st.session_state.celebration_for == challenge_id:
    st.balloons()
    st.session_state.celebration_for = None

with st.container(border=True):
    st.markdown(f'<div class="challenge-kicker">Reto {challenge_number + 1} · {subject}</div>', unsafe_allow_html=True)

    if subject == "Lectura":
        st.markdown('<div class="challenge-title">¿Qué vocal falta?</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="challenge-copy">Mira el dibujo, lee la pista y elige la vocal correcta.</div>',
            unsafe_allow_html=True,
        )
        st.markdown(f'<div class="picture-emoji">{challenge["emoji"]}</div>', unsafe_allow_html=True)
        letters = "".join(
            f'<span class="missing-letter">?</span>' if letter == "_" else letter
            for letter in challenge["pattern"]
        )
        st.markdown(f'<div class="word-display">{letters}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="hint-pill">💡 {challenge["hint"]}</div>', unsafe_allow_html=True)
        options = ["A", "E", "I", "O", "U"]
        columns = st.columns(len(options))
        for column, vowel in zip(columns, options):
            with column:
                st.button(
                    vowel,
                    key=f"{challenge_id}-option-{vowel}",
                    use_container_width=True,
                    disabled=solved,
                    on_click=submit_answer,
                    args=(challenge_id, vowel, challenge["answer"]),
                )
    else:
        if challenge["kind"] == "count":
            st.markdown('<div class="challenge-title">¡Vamos a contar!</div>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="challenge-copy">Cuenta todos los objetos y descubre cuántos hay.</div>',
                unsafe_allow_html=True,
            )
            object_html = "".join(
                f'<span class="count-object">{challenge["emoji"]}</span>'
                for _ in range(challenge["count"])
            )
            st.markdown(
                f'<div class="objects-board" role="img" aria-label="{challenge["count"]} {challenge["label"]}">{object_html}</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="challenge-copy" style="text-align:center; font-weight:800;">¿Cuántas {challenge["label"]} ves?</div>',
                unsafe_allow_html=True,
            )
            answer = challenge["count"]
        else:
            st.markdown('<div class="challenge-title">¡Resolvamos una suma!</div>', unsafe_allow_html=True)
            st.markdown(
                '<div class="challenge-copy">Junta los dos grupos y encuentra el total.</div>',
                unsafe_allow_html=True,
            )
            answer = challenge["left"] + challenge["right"]
            st.markdown(
                f'<div class="sum-display"><span class="sum-number">{challenge["left"]}</span><span class="sum-plus">+</span><span class="sum-number">{challenge["right"]}</span><span>=</span><span>?</span></div>',
                unsafe_allow_html=True,
            )

        choices = {answer}
        distance = 1
        while len(choices) < 4:
            choices.add(max(0, answer - distance))
            choices.add(answer + distance)
            distance += 1
        choices = list(choices)
        random.Random(challenge_id).shuffle(choices)
        columns = st.columns(len(choices))
        for column, value in zip(columns, choices):
            with column:
                st.button(
                    str(value),
                    key=f"{challenge_id}-option-{value}",
                    use_container_width=True,
                    disabled=solved,
                    on_click=submit_answer,
                    args=(challenge_id, value, answer),
                )

    if solved:
        st.success("¡Muy bien! Búho Sabio está orgulloso de ti. ¡Ganaste 10 puntos! 🎉")
        if st.button("🌟 ¡Quiero otro reto!", key=f"{challenge_id}-next", use_container_width=True):
            st.session_state.activity_index += 1
            st.session_state.last_try = None
            st.rerun()
    elif st.session_state.last_try == challenge_id:
        st.warning("¡Casi! Inténtalo otra vez. Búho Sabio sabe que puedes. 💪")

st.markdown(
    '<div style="text-align:center; color:#8790a8; font-size:.88rem; margin-top:1.4rem;">Aprender también es jugar. ¡Sigue brillando! ✨</div>',
    unsafe_allow_html=True,
)
```
