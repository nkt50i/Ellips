import streamlit as st

menu = st.sidebar.radio('***',
    ("Комплексный потенциал течения", 
    "Критические точки",       
    "Аналитическое решение",
    "Решение методом конечных элементов (FEM)",
    "Циркулляция",
    "Программная реализация",
    )
)

if menu == "Комплексный потенциал течения":
    
    st.markdown('<h3 style="text-align: center;">Комплексный потенциал течения</h3>', unsafe_allow_html=True)
    st.markdown(r"""
    
    
    $$ 
    w = u_{\infty} \left(z + \frac{a^2}{z}\right) + \frac{\Gamma}{2 \pi i} \ln{z}, \quad z \in \mathbb{C} 
    $$

    **где**:
    * $a$ — радиус круглого цилиндра,
    * $\displaystyle u_{\infty} = u_{x_1} + i u_{x_2}$,
    * $\displaystyle z = x_1 + i x_2$.

    Второе слагаемое представляет собой комплексный потенциал вихря с циркуляцией $\Gamma$:
    
    $$ 
    w_{vortex} =  \frac{\Gamma}{2 \pi i} \ln{z} 
    $$
    """)

    st.markdown('<h3 style="text-align: center;">Комплексно-сопряженная скорость</h3>', unsafe_allow_html=True)
    st.markdown(r"""
    $$ 
    \frac{d w}{d z} = u_{x_1} - i u_{x_2} = u_{\infty} \left(1 - \frac{a^2}{z^2}\right) +  \frac{\Gamma}{2 \pi i} \frac{1}{z} 
    $$

    **где**:
    * $\text{Re } \frac{d w}{ d z} = u_{x_1}$,
    * $\text{Im } \frac{d w}{ d z} = - u_{x_2}$.

    Так как все линии тока от вихря — это окружности с центром в начале координат, добавление этого потенциала не нарушит условий непротекания цилиндра.
    """)

    st.markdown('<h3 style="text-align: center;">Бесциркулляционное течение</h3>', unsafe_allow_html=True)
    st.markdown(r"""
    При $\Gamma = 0$:
    
    $$ 
    w_{vortex} = 0 
    $$
    
    $$ 
    w = u_{\infty} \left(z + \frac{a^2}{z}\right), \quad |z| > a 
    $$

    $$ 
    \frac{d w}{d z} = u_{\infty} \left(1 - \frac{a^2}{z^2}\right) 
    $$

    """)

elif menu == "Критические точки":

    st.markdown('<h3 style="text-align: center;">Критические точки</h3>', unsafe_allow_html=True)
    st.markdown(r"""

    Определим положение критических точек, решив уравнение:
    
    $$ 
    u_{\infty} \left(1 - \frac{a^2}{z^2}\right) + \frac{\Gamma}{2 \pi i} \frac{1}{z} = 0 
    $$

    Это уравнение сводится к квадратному:

    $$ 
    z^2 - \frac{\Gamma i}{2 \pi u_{\infty}} z - a^2 = 0 
    $$

    Решение:
    
    $$ 
    z_{1,2} = \frac{\Gamma i}{4 \pi u_{\infty}} \pm \sqrt{a^2 - \frac{\Gamma^2}{16 \pi^2 u^2_{\infty}}} 
    $$

    """)

    subtopic = st.selectbox(
        "Выберите случай",  
        ["1. Оба корня чисто мнимые и лежат на мнимой оси", "2. Кратные корни", "3. Комплексные корни", "4. Бесциркулляционное течение"]  
    )

    if subtopic == "1. Оба корня чисто мнимые и лежат на мнимой оси":
        st.markdown(r"""
        $$ 
        \Gamma > 4 \pi u_{\infty} a 
        $$
        
        $$ 
        z_1 = i \left[\frac{\Gamma i}{4 \pi u_{\infty}} + \sqrt{\frac{\Gamma^2}{16 \pi^2 u^2_{\infty}} - a^2}\right] 
        $$

        $$ 
        \text{Im } z_1 > \frac{\Gamma}{4 \pi u_{\infty}} > a 
        $$

        $$ 
        z_2 = i \left[\frac{\Gamma i}{4 \pi u_{\infty}} - \sqrt{\frac{\Gamma^2}{16 \pi^2 u^2_{\infty}} - a^2}\right] 
        $$

        Второй корень находится внутри круга и не представляет для нас никакого смысла.
        """)

    elif subtopic == "2. Кратные корни":
        st.markdown(r"""
        $$ 
        \Gamma = 4 \pi u_{\infty} a 
        $$
        
        $$ 
        z_1 = z_2 = i a 
        $$
        
        Корни сливаются между собой и расположены в наивысшей точке цилиндра.
        """)

    elif subtopic == "3. Комплексные корни":
        st.markdown(r"""
        $$ 
        \Gamma < 4 \pi u_{\infty} a 
        $$
        
        $$ 
        z_1 = \frac{\Gamma i}{4 \pi u_{\infty}} + \sqrt{a^2 - \frac{\Gamma^2}{16 \pi^2 u^2_{\infty}}} 
        $$

        $$ 
        z_2 = \frac{\Gamma i}{4 \pi u_{\infty}} - \sqrt{a^2 - \frac{\Gamma^2}{16 \pi^2 u^2_{\infty}}} 
        $$

        Корни расположены симметрично относительно оси $x_2$. Оба корня лежат на окружности, так как:
        
        $$ 
        |z_1| = |z_2| = a 
        $$
        """)

    elif subtopic == "4. Бесциркулляционное течение":
        st.markdown(r"""
        $$ 
        u_{\infty} \left(1 - \frac{a^2}{z^2}\right) = 0 
        $$

        $$ 
        z_1 = a 
        $$

        $$ 
        z_2 = - a 
        $$
        """)


elif menu == "Аналитическое решение":
    st.markdown('<h3 style="text-align: center;">Аналитическое решение</h3>', unsafe_allow_html=True)

    st.image("circulation_cylinder.png", caption="", width=850)

    r"""
    * Радиус цилиндра: $a = 0.125$
    * Скорость на входе: $u_{\infty} = 1$

    ------------------------------------------------
    """
    st.markdown('<h3 style="text-align: center;">Критические точки</h3>', unsafe_allow_html=True)
  
    st.markdown(r"""

        $$ 
        x_1 = 0.375, \quad x_2 = 0.5
        $$

        $$ 
        x_1 = 0.625, \quad x_2 = 0.5
        $$
        """)
        
    st.markdown('<h3 style="text-align: center;">Циркулляция</h3>', unsafe_allow_html=True)

    st.markdown(r"""

        $$ 
        \Gamma = 0
        $$

        """)

    with st.expander("Функция комплексного потенциала и комплексно-сопряженной скорости"):
        code = """
        def velocity_field(x, y):
            z = (x - cx) + 1j * (y - cy)
            if np.abs(z) < c:  # Если точка внутри цилиндра, возвращаем NaN
                return np.nan, np.nan
            w_prime = vinf * (np.exp(-1j * alpha_rad) - c**2 / z**2 * np.exp(1j * alpha_rad))
            return np.real(w_prime), -np.imag(w_prime)
        """

        st.code(code, language="python")

    with st.expander("Поиск критических точек"):
        code = """
        def stagnation_eq(x):
            x = x[0]  # Берём первый элемент массива
            z = complex(x - cx, cy - cy)  # Только x-координата меняется, y=cy
            w_prime = vinf * (np.exp(-1j * alpha_rad) - c**2 / z**2 * np.exp(1j * alpha_rad))
            return np.real(w_prime)  # Должно быть равно 0

            # Ищем два корня (левый и правый стагнационные точки)
            stagnation_x1 = fsolve(stagnation_eq, cx + c)[0]
            stagnation_x2 = fsolve(stagnation_eq, cx - c)[0]
            stagnation_points = np.array([[stagnation_x1, cy], [stagnation_x2, cy]])
            """

        st.code(code, language="python")

    with st.expander("Вычисление поля скоростей"):
        code = """
        
        U, V = np.vectorize(velocity_field)(X, Y)

        speed = np.sqrt(np.abs(U)**2 + np.abs(V)**2)
        """

        st.code(code, language="python")

elif menu == "Решение методом конечных элементов (FEM)":

    r"""

    ##### Решение методом конечных элементов (FEM)

    """

    subtopic = st.selectbox(
        "Размер сетки",  
        ["712", "2958", "13746"]  
    )

    if subtopic == "712":
        
        st.image("ellips_1.png", caption="",width=1000)

        r"""
        * Число ячеек сетки: 712

        * Число узлов сетки: 396

        ------------------------------------------------
        """
        st.image("ellips_solve_1.png", caption="",width=800)

    elif subtopic == "2958":

        st.image("ellips_2.png", caption="",width=1000)

        r"""
        * Число ячеек сетки: 2968

        * Число узлов сетки: 1636

        ------------------------------------------------
        """
        st.image("ellips_solve_2.png", caption="",width=800)

    elif subtopic == "13746":

        st.image("ellips_3.png", caption="",width=1000)

        r"""
        * Число ячеек сетки: 13746

        * Число узлов сетки: 7307

        ------------------------------------------------
        """
        st.image("ellips_solve_3.png", caption="",width=800)


elif menu == "Циркулляция":

    st.markdown(r"""
    <div style="display: flex; justify-content: center;">
        <div style="width: 90%; font-size: 20px;">
            <h3 style="text-align: center;">Циркулляция</h3>
            <table style="width: 100%; border-collapse: collapse; margin: 0 auto; font-family: Arial, sans-serif;">
                <thead>
                    <tr>
                        <th style="border: 1px solid #ddd; padding: 12px; text-align: center; font-weight: bold; background-color: #f2f2f2;">Размер сетки</th>
                        <th style="border: 1px solid #ddd; padding: 12px; text-align: center; font-weight: bold; background-color: #f2f2f2;">p = 1</th>
                        <th style="border: 1px solid #ddd; padding: 12px; text-align: center; font-weight: bold; background-color: #f2f2f2;">p = 2</th>
                        <th style="border: 1px solid #ddd; padding: 12px; text-align: center; font-weight: bold; background-color: #f2f2f2;">p = 3</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center; font-weight: bold;">712</td>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center;">-1.29200e<sup>-04</sup></td>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center;">-7.53011e<sup>-05</sup></td>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center;">-3.96871e<sup>-05</sup></td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center; font-weight: bold;">2968</td>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center;">8.61544e<sup>-07</sup></td>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center;">1.19674e<sup>-05</sup></td>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center;">7.68601e<sup>-06</sup></td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center; font-weight: bold;">13746</td>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center;">2.88749e<sup>-06</sup></td>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center;">1.19933e<sup>-06</sup></td>
                        <td style="border: 1px solid #ddd; padding: 12px; text-align: center;">8.54737e<sup>-07</sup></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif menu == "Программная реализация":
    r"""
    ### Программная реализация
    """

    with st.expander("Определение функционального пространства"):
        code = """
            V = FunctionSpace(mesh, "CG", 1)
        """
        st.code(code, language="python")

    with st.expander("Условие на входе в канал"):
        code = """
            u_infinity = Expression("x[1]", degree=2)
            H = 1
            psi_0 = u_infinity * H
        """
        st.code(code, language="python")

    with st.expander("Граничные условия"):
        code = """
        bcs = [DirichletBC(V, Constant(0.0), boundaries, 1), 
                DirichletBC(V, u_infinity * H, boundaries, 2),
                DirichletBC(V, Constant(0.5), boundaries, 5),
                DirichletBC(V, u_infinity * H, boundaries, 3),
                DirichletBC(V, u_infinity * H, boundaries, 4)]
        """
        st.code(code, language="python")

    with st.expander("Вариационная задача"):
        code = """
            u = TrialFunction(V)
            v = TestFunction(V)
            f = Constant(0.0)
            a = dot(grad(u), grad(v)) * dx
            L = f * v * dx
        """
        st.code(code, language="python")

    with st.expander("Решение задачи"):
        code = """
            u = Function(V)
            solve(a == L, u, bcs)
        """
        st.code(code, language="python")

    with st.expander("Вычисление скорости"):
        code = """
            V_vector = VectorFunctionSpace(mesh, "CG", 3)
            velocity = project(grad(u), V_vector)
            velocity_magnitude = project(sqrt(dot(velocity, velocity)), V)
        """
        st.code(code, language="python")

    with st.expander("Вычисление циркуляции"):
        code = """
            n = FacetNormal(mesh)
            u_n = dot(grad(u), n)
            Gamma = assemble(u_n * ds(subdomain_data=boundaries, subdomain_id=5))
        """
        st.code(code, language="python")

    with st.expander("Поиск критических точек"):
        code = """
            threshold = 1e-15
            critical_points = (velocity_values <threshold) """ 
            
        
        st.code(code, language="python")
