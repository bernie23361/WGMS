import gradio as gr
import os
from login_ui import create_login_ui
from dashboard_ui import create_dashboard_ui

# 從 Secret 抓取剛才設定的隱藏帳密
USER_ACCOUNT = os.getenv("WGMS_USER")
USER_PASSWORD = os.getenv("WGMS_PW")

def handle_login(u, p):
    if u == USER_ACCOUNT and p == USER_PASSWORD:
        # 成功：關掉門面，打開主頁
        return gr.update(visible=False), gr.update(visible=True), ""
    else:
        # 失敗：觸發您設計的紅框狀態與抖動
        return gr.update(visible=True, elem_classes="login-card error-shake"), gr.update(visible=False), "⚠️ 登錄錯誤！請再重試一次..."

with gr.Blocks(css="/* 這裡周一我幫您填入完整的 XD 樣式 */") as demo:
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
