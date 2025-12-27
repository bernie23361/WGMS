import gradio as gr

def create_login_ui():
    gr.Markdown("# WGMS 氣象地動監測平台")
    with gr.Column(elem_classes="login-card"):
        # 對應您 XD 裡的帳號密碼框
        user = gr.Textbox(label="用戶名", placeholder="請輸入用戶名")
        pw = gr.Textbox(label="密碼", type="password", placeholder="請輸入密碼")
        
        # 蘇老闆設計的「記住密碼」
        remember = gr.Checkbox(label="記住密碼", value=False)
        
        login_btn = gr.Button("登錄", elem_classes="login-btn")
        error_msg = gr.Markdown("", visible=False)
        
        gr.Markdown("天氣概況Weather工作室版權所有．", elem_id="copyright")
        
    return {"user": user, "pass": pw, "btn": login_btn, "error": error_msg}
