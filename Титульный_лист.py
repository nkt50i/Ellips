import streamlit as st

st.set_page_config(page_title="👋", layout="wide")

st.markdown("""
    <h1 style="text-align:center; font-size: 50px;">Филиал Московского государственного университета имени М. В. Ломоносова в городе Сарове</h1>
""", unsafe_allow_html=True)
st.markdown("""
    <h1 style="text-align:center; font-size: 40px;">Кафедра математики</h1>
""", unsafe_allow_html=True)
st.markdown("""
    <h1 style="text-align:center; font-size: 35px;">Группа ВМ - 124</h1>
""", unsafe_allow_html=True)

# Дополнительное изображение по центру
st.image("logo.jpg", width=300, use_container_width=True)

st.markdown("""
    <h1 style="text-align:center; font-size: 50px;">Численное исследование потенциального обтекания пучка цилиндров эллиптического сечения</h1>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style="text-align:left; font-size: 35px;">Презентацию подготовили:</h1>
""", unsafe_allow_html=True)

# Данные участников
participants = [
    {"name": "Головня Никита", "photo": "0.jpeg"},
    {"name": "Александр Романенко", "photo": "1.jpeg"},
    {"name": "Гашигуллин Камиль", "photo": "2.jpeg"},
    {"name": "Коврижных Анастасия", "photo": "3.jpeg"},
    {"name": "Сержантов Артемий", "photo": "4.jpeg"},
    
]

# Вывод участников в две строки
row1 = participants[:3]  
row2 = participants[3:]  

cols1 = st.columns(3)
for i, participant in enumerate(row1):
    with cols1[i]:
        st.image(participant["photo"], width=200)
        st.markdown(f"""
            <h3 style="margin: 0; text-align: left;">{participant['name']}</h3>
        """, unsafe_allow_html=True)

cols2 = st.columns(3)
for i, participant in enumerate(row2):
    with cols2[i]:
        st.image(participant["photo"], width=200)
        st.markdown(f"""
            <h3 style="margin: 0; text-align: left;">{participant['name']}</h3>
        """, unsafe_allow_html=True)

st.markdown("""
    <h2 style="text-align:left;">О презентации</h2>
    <p style="text-align:left; font-size: 18px;">
        Исследование потенциального обтекания пучков цилиндров эллиптического сечения представляет собой
             важную задачу теоретической и прикладной аэрогидродинамики. Такие течения встречаются в
             широком спектре инженерных приложений, включая конструкции теплообменников, элементы
             гидродинамических систем и аэродинамические структуры. 
    </p>
    <p style="text-align:left; font-size: 18px;">
        Данный проект можно посмотреть и скачать на 
        <a href="https://github.com/nkt50i/Ellips" target="_blank" style="font-weight: bold;">
        GitHub</a>.
    </p>
    <p style="text-align:left; font-size: 18px; font-weight: bold;">
        ❗❗❗ Все ссылки в презентации работают только с VPN ❗❗❗
    </p>
""", unsafe_allow_html=True)
