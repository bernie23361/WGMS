import gradio as gr

def create_login_ui():
    gr.Markdown("# WGMS 氣象地動監測平台")
    with gr.Column(elem_classes="login-card"):
        user = gr.Textbox(label="帳號", placeholder="請輸入 weather0215")
        pw = gr.Textbox(label="密碼", type="password", placeholder="請輸入密碼")
        
        # 蘇老闆要求的：記住密碼與圖示預留
        with gr.Row():
            remember = gr.Checkbox(label="記住密碼", value=False)
            
        login_btn = gr.Button("進入系統", elem_classes="login-btn")
        error_msg = gr.Markdown("", visible=False)
        
    return {"user": user, "pass": pw, "btn": login_btn, "error": error_msg}
