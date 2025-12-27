import gradio as gr
import os
from login_ui import create_login_ui
from dashboard_ui import create_dashboard_ui

# 這裡會去抓 Hugging Face 裡的 Secret
USER_ACCOUNT = os.getenv("WGMS_USER")
USER_PASSWORD = os.getenv("WGMS_PW")

def handle_login(u, p):
    if u == USER_ACCOUNT and p == USER_PASSWORD:
        return gr.update(visible=False), gr.update(visible=True), ""
    else:
        return gr.update(visible=True, elem_classes="error-shake"), gr.update(visible=False), "⚠️ 登錄錯誤"

with gr.Blocks() as demo:
    with gr.Column(visible=True) as login_layout:
        login_view = create_login_ui()
    with gr.Column(visible=False) as dashboard_layout:
        create_dashboard_ui()

    login_view['btn'].click(
        handle_login,
        inputs=[login_view['user'], login_view['pass']],
        outputs=[login_layout, dashboard_layout, login_view['error']]
    )

demo.launch()
