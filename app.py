import streamlit  as st
from st_ant_carousel import st_ant_carousel
from typing import Dict

st.set_page_config(layout="wide")

def create_slide(text: str, background_color: str) -> Dict:
    return {
        "style": {
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "fontFamily": "Arial, sans-serif",
            "background-color": background_color,
            "padding": "30px",
        },
        "content": f"<h2 style='color: #FFFFFF; font-size: 30px; text-align: center;'>{text}</h2>",
    }

default_content = [
    create_slide("Welcome to Our Website", "#2ECC71"),
    create_slide("Featured Article", "#3498DB"),
    create_slide("Explore Our Gallery", "#9B59B6"),]

st.title("Carousel Component Example")

st.sidebar.header("Carousel Configuration")

autoplay = st.sidebar.checkbox("Autoplay", value=True)
autoplay_speed = st.sidebar.number_input("Autoplay Speed", value=3000, min_value=1, max_value=10000)
st.sidebar.caption("Autoplay Speed sets the interval in milliseconds for automatic scrolling")

dot_position = st.sidebar.selectbox("Dot Position", ["top", "bottom", "left", "right"])
dots = st.sidebar.checkbox("Show Dots", value=True)
animation_speed = st.sidebar.number_input("Animation Speed", value=500, min_value=1, max_value=10000)
st.sidebar.caption("Animation Speed sets the duration in milliseconds for transition animations")


waitForAnimate = st.sidebar.checkbox("Wait for Animate", value=True)
easing = st.sidebar.selectbox("Easing", ["linear", "ease", "ease-in", "ease-out", "ease-in-out"])
effect = st.sidebar.selectbox("Effect", ["scrollx", "fade"])
pauseOnDotsHover = st.sidebar.checkbox("Pause on Dots Hover", value=False)
pauseOnHover = st.sidebar.checkbox("Pause on Hover", value=True)
vertical = st.sidebar.checkbox("Vertical")
adaptive_height = st.sidebar.checkbox("Adaptive Height")

st.sidebar.info("When Vertical is checked, the carousel will scroll vertically instead of horizontally. Make sure to set Dot Position to 'left' or 'right' if you enable Vertical.")

st.sidebar.header("Carousel Style")
bg_color = st.sidebar.color_picker("Background Color", value="#f0f2f5")
border_radius = st.sidebar.slider("Border Radius", value=8, min_value=0, max_value=20)
box_shadow_intensity = st.sidebar.slider("Box Shadow Intensity", value=0.1, min_value=0.0, max_value=1.0, step=0.05)
padding = st.sidebar.slider("Padding", value=20, min_value=0, max_value=50)

st.sidebar.header("Dot Style")
dot_color = st.sidebar.color_picker("Dot Color", value="#a8a9ab")
active_dot_color = st.sidebar.color_picker("Active Dot Color", value="#78797a")

carousel_style = {
    "background-color": bg_color,
    "border-radius": f"{border_radius}px",
    "box-shadow": f"0 4px 6px rgba(0, 0, 0, {box_shadow_intensity})",
    "padding": f"{padding}px",
    "customCss": f"""
        .ant-carousel .slick-dots li button {{
            background-color: {dot_color} !important;
        }}
        .ant-carousel .slick-dots li.slick-active button {{
            background-color: {active_dot_color} !important;
        }}
    """
}


carousel_args = {
    "content": default_content,
    "carousel_style": carousel_style,
    "autoplay": autoplay,
    "autoplaySpeed": autoplay_speed,
    "dotPosition": dot_position,
    "dots": dots,
    "waitForAnimate": waitForAnimate,
    "easing": easing,
    "effect": effect,
    "pauseOnDotsHover": pauseOnDotsHover,
    "pauseOnHover": pauseOnHover,
    "animationSpeed": animation_speed,
    "vertical": vertical,
    "adaptiveHeight": adaptive_height,
}

st_ant_carousel(**carousel_args)

st.header("Final CSS Code")
st.code(carousel_style, language="css")


st.header("Content Code")
st.code(default_content, language="python")

st.header("Function Call")
st.code(f"""
st_ant_carousel(
    content={default_content},
    carousel_style={carousel_style},
    autoplay={autoplay},
    autoplaySpeed={autoplay_speed},
    dotPosition="{dot_position}",
    dots={dots},
    waitForAnimate={waitForAnimate},
    easing="{easing}",
    effect="{effect}",
    pauseOnDotsHover={pauseOnDotsHover},
    pauseOnHover={pauseOnHover},
    animationSpeed={animation_speed},
    vertical={vertical},
    adaptiveHeight={adaptive_height},
)
""")

