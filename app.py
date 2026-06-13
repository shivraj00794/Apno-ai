import gradio as gr
import g4f

def munim_ji_bot(grahak, paisa, dukan):
    munim_rules = f"तुम 'आपणो एआई' के मुनीम जी हो। उधार का व्हाट्सएप मैसेज मिक्स हिंदी-मारवाड़ी में बनाओ। फॉर्मेट: '[नाम] जी नमस्कार, आपके [पैसे] ₹ का खाता बाकी चल रहा है। कृपा करके दुकान पर आकर हिसाब क्लियर करवाएं सा। - {dukan} सा।'"
    prompt = f"डेटा: {grahak} का {paisa} रुपया बाकी है, दुकान का नाम {dukan} है"
    try:
        return g4f.ChatCompletion.create(model="gpt-4o", messages=[{"role": "system", "content": munim_rules}, {"role": "user", "content": prompt}])
    except:
        return f"{grahak} जी नमस्कार, आपके {paisa} ₹ का खाता बाकी चल रहा है। कृपा करके दुकान पर आकर हिसाब क्लियर करवाएं सा। - {dukan} सा।"

def student_bot(selected_class, topic):
    student_rules = f"तुम 'आपणो एआई' के ऑल-इन-वन स्टडी पार्टनर हो। तुम अभी कक्षा {selected_class} के बच्चे को पढ़ा रहे हो। उसके लेवल के हिसाब से उसके मुश्किल सवाल को एकदम आसान पॉइंट-बाय-पॉइंट हिंदी-मारवाड़ी मिक्स भाषा में समझाओ।"
    try:
        return g4f.ChatCompletion.create(model="gpt-4o", messages=[{"role": "system", "content": student_rules}, {"role": "user", "content": topic}])
    except:
        return f"भाई साहब, कक्षा {selected_class} के इस टॉपिक ({topic}) का सीधा मतलब है कि सब काम मिल-बांट कर करना सा!"

custom_css = """
body { background-color: #ffffff !important; }
.gradio-container { max-width: 750px !important; margin: 0 auto !important; font-family: 'Poppins', sans-serif !important; background-color: #ffffff !important; }
h1 { text-align: center !important; color: #0066cc !important; font-weight: 800 !important; }
h3 { text-align: center !important; color: #444444 !important; font-size: 1.1rem !important; margin-bottom: 20px !important; }
.tabs { background: #e6f0fa !important; border-radius: 15px !important; padding: 15px !important; border: 1px solid #c8dcff !important; }
.tab-nav button { color: #444444 !important; border-radius: 8px !important; font-weight: 600 !important; margin: 2px !important; }
.tab-nav button.selected { background: linear-gradient(135deg, #0066cc, #00bfff) !important; color: white !important; }
input, textarea, select { background-color: #f0f7ff !important; color: #111111 !important; border: 1px solid #b8d5ff !important; border-radius: 10px !important; padding: 12px !important; }
button.primary { background: linear-gradient(135deg, #0066cc, #00bfff) !important; color: white !important; font-weight: 700 !important; border: none !important; border-radius: 12px !important; }
footer { display: none !important; }
.custom-footer { text-align: center !important; color: #000000 !important; margin-top: 35px !important; font-size: 1.05rem !important; background-color: #ffffff !important; border-top: 1px solid #e0e0e0 !important; padding: 15px !important; }
"""

with gr.Blocks(css=custom_css) as aapno_app:
    gr.Markdown("# 🤖 आपणो एआई (Aapno AI)")
    gr.Markdown("### 💎 साभार: शिवराज जाट द्वारा निर्मित (Powered by Shivraj Jat)")
    with gr.Tabs(elem_classes="tabs"):
        with gr.Tab("🏪 बिज़नेस मुनीम जी"):
            grahak_input = gr.Textbox(label="👤 ग्राहक का नाम", placeholder="ग्राहक का नाम लिखें सा...")
            paisa_input = gr.Textbox(label="💰 बाकी उधार (₹)", placeholder="कितने पैसे बाकी हैं सा...")
            dukan_input = gr.Textbox(label="🏢 दुकान/बिज़नेस का नाम", value="शिवराज जी")
            munim_btn = gr.Button("व्हाट्सएप मैसेज बनाएं सा", variant="primary")
            munim_output = gr.Textbox(label="📝 मुनीम जी का संदेश", lines=3)
            munim_btn.click(munim_ji_bot, inputs=[grahak_input, paisa_input, dukan_input], outputs=munim_output)
        with gr.Tab("📚 स्टूडेंट स्टडी पार्टनर"):
            class_dropdown = gr.Dropdown(label="🎓 अपनी क्लास चुनिए सा 👇", choices=["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"], value="10th")
            topic_input = gr.Textbox(label="❓ अपनी पढ़ाई का कोई भी सवाल या टॉपिक यहाँ लिखें सा?", placeholder="जैसे: संघीय व्यवस्था क्या है?")
            student_btn = gr.Button("आसान भाषा में समझाइए सा", variant="primary")
            student_output = gr.Textbox(label="💡 स्टूडेंट पार्टनर का जवाब", lines=6)
            student_btn.click(student_bot, inputs=[class_dropdown, topic_input], outputs=student_output)
    gr.HTML("<div class='custom-footer'>© 2026 आपणो एआई। ऑल राइट्स रिजर्व्ड। <br>🚀 <b>मुख्य डेवलपर: शिवराज जाट (Shivraj Jat)</b></div>")

aapno_app.launch()
