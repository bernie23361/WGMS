import gradio as gr
import os
from login_ui import create_login_ui
from dashboard_ui import create_dashboard_ui

# 從 Hugging Face 的 Secrets 讀取隱藏帳密 (安全防護)
USER_ACCOUNT = os.getenv("WGMS_USER")
USER_PASSWORD = os.getenv("WGMS_PW")

def handle_login(u, p):
    if u == USER_ACCOUNT and p == USER_PASSWORD:
        # 登錄成功：隱藏登錄頁，顯示主頁
        return gr.update(visible=False), gr.update(visible=True), ""
    else:
        # 登錄失敗：保持登錄頁顯示，並觸發紅框抖動 (透過 CSS Class)
        return gr.update(visible=True, elem_classes="error-shake"), gr.update(visible=False), "⚠️ 驗證失敗，請檢查帳號密碼"

with gr.Blocks(css=os.getenv("CUSTOM_CSS", "")) as demo:
    # 登錄頁容器
    with gr.Column(visible=True) as login_layout:
        login_components = create_login_ui()
        
    # 主頁面容器 (初始隱藏)
    with gr.Column(visible=False) as dashboard_layout:
        create_dashboard_ui()

    # 點擊事件：連接大腦與 UI
    login_components['btn'].click(
        handle_login,
        inputs=[login_components['user'], login_components['pass']],
        outputs=[login_layout, dashboard_layout, login_components['error']]
    )

demo.launch()
