import streamlit as st

menu = st.sidebar.radio('***',
    ("Комплексный потенциал течения", 
    "Критические точки",       
    "Аналитическое решение",
    )
)

if menu == "Комплексный потенциал течения":
    r"""
    ##### Комплексный потенциал течения
    Возьмём комплексный потенциал в виде
    
    $\begin{aligned}
    w = u_{\infty} \left(z + \frac{a^2}{z}\right) + \frac{\Gamma}{2 \pi i} \ln{z}, z \in  \mathbb{C}
    \end{aligned}$

    $\begin{aligned}
    z = x_1 + i x_2
    \end{aligned}$

     * $a$ - ридиус круглого цилиндра

    Второе слагаемое представляет собой комплексный потенциал вихря с циркуляцией $\Gamma$
    
    $\begin{aligned}
    w_{vortex} =  \frac{\Gamma}{2 \pi i} \ln{z}
    \end{aligned}$

    Определим компоненты вектора скорости

    $\begin{aligned}
    \frac{d w}{d z} = u_x - i u_y
    \end{aligned}$

    $\begin{aligned}    
    \text{Re } \frac{d w}{ d z} = u_x
    \end{aligned}$

    $\begin{aligned}    
    \text{Im } \frac{d w}{ d z} = - u_y
    \end{aligned}$

    $\begin{aligned}
    \frac{d w}{d z} = u_{\infty} \left(1 - \frac{a^2}{z^2}\right) \frac{\Gamma}{2 \pi i} \frac{1}{z}
    \end{aligned}$

    Так как все линии тока от вихря – это окружности с центром вначале координат, то ясно, что добавление этого потенциала не нарушит условий непротекания цилиндра.
    """

elif menu == "Критические точки":
    r"""
    ##### Критические точки

    Определим положение критических точек, решив уравнение
    
    $\begin{aligned}
    u_{\infty} \left(1 - \frac{a^2}{z^2}\right) \frac{\Gamma}{2 \pi i} \frac{1}{z} = 0
    \end{aligned}$

    Оно сводится к квадратному

    $\begin{aligned}
    z^2 - \frac{\Gamma i}{2 \pi u_{\infty}} z - a^2 = 0
    \end{aligned}$

    $\begin{aligned}
    z_{1,2} = \frac{\Gamma i}{4 \pi u_{\infty}} \pm \sqrt{a^2 - \frac{\Gamma^2}{16 \pi^2 u^2_{\infty}}}
    \end{aligned}$
    """

    subtopic = st.selectbox(
        "Выберите случай",  
        ["1. Оба корня чисто мнимые и лежат на мнимой оси", "2. Кратные корни", "3. Комплексные корни"]  
    )

    if subtopic == "1. Оба корня чисто мнимые и лежат на мнимой оси":
        r"""
        $\begin{aligned}
        \Gamma > 4 \pi u_{\infty} a
        \end{aligned}$

        $\begin{aligned}
        z_1 = i \left[\frac{\Gamma i}{4 \pi u_{\infty}} + \sqrt{\frac{\Gamma^2}{16 \pi^2 vu^2_{\infty}} - a^2}\right]
        \end{aligned}$

        $\begin{aligned}
        \text{Im } z_1 > \frac{\Gamma}{4 \pi u_{\infty}} > a
        \end{aligned}$

        $\begin{aligned}
        z_2 = i \left[\frac{\Gamma i}{4 \pi u_{\infty}} - \sqrt{\frac{\Gamma^2}{16 \pi^2 u^2_{\infty}} - a^2}\right]
        \end{aligned}$

        $\begin{aligned}
        \text{Im } z_2 = \frac{a^2}{\frac{\Gamma}{4 \pi u_{\infty}} + \sqrt{\frac{\Gamma^2}{16 \pi^2 u_{\infty}^2} - a^2}} < \frac{a^2}{\Gamma^2 / (4 \pi u_{\infty})} < \frac{a^2}{a} < a
        \end{aligned}$ 

        Второй корень находится внутри круга и не представляет для нас никакого смысла.
        """

    elif subtopic == "2. Кратные корни":
        r"""
        $\begin{aligned}
        \Gamma = 4 \pi u_{\infty} a
        \end{aligned}$

        $\begin{aligned}
        z_1 = z_2 = i a
        \end{aligned}$

        Корни сливаются между собой и расположены в наивысшей точке цилиндра.
        """

    elif subtopic == "3. Комплексные корни":
        r"""
        $\begin{aligned}
        \Gamma < 4 \pi u_{\infty} a
        \end{aligned}$

        $\begin{aligned}
        z_1 = \frac{\Gamma i}{4 \pi u_{\infty}} + \sqrt{a^2 - \frac{\Gamma^2}{16 \pi^2 u^2_{\infty}}}
        \end{aligned}$

        $\begin{aligned}
        z_2 = \frac{\Gamma i}{4 \pi u_{\infty}} - \sqrt{a^2 - \frac{\Gamma^2}{16 \pi^2 u^2_{\infty}}}
        \end{aligned}$

        Корни расположены симметрично относительно оси $x_2$. Оба корня лежат на окружности, так как

        $\begin{aligned}
        |z_1| = |z_2| = a
        \end{aligned}$
        """

elif menu == "Аналитическое решение":
    r"""
    ##### Аналитическое решение
    """

    st.image("circulation_cylinder.png", caption="",use_container_width=True)

    r"""
     * Радиус цилиндра: $a = 0.125$
     * Скорость на входе: $u_{\infty} = 1$

     ------------------------------------------------
    ##### Критические точки
    $x_1 = 0.375, x_2 = 0.5$
    
    $x_1 = 0.625, x_2 = 0.5$
    ##### Циркулляция
    $\Gamma = 0$
    """
