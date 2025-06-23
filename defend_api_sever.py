from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB까지 허용
CORS(app)

# ✅ Google Gemini API 키 설정
genai.configure(api_key="AIzaSyBbE8WtD3uXI2eYp-lrISHk5myuNBjGSao")

# ✅ Gemini Vision 모델 초기화
model = genai.GenerativeModel("gemini-pro-vision")

@app.route('/analyze-image', methods=['POST', 'OPTIONS'])
def analyze_image():
    try:
        data = request.json
        image_base64 = data.get('imageBase64', '')
        mime_type = data.get('mimeType', '')

        # ✅ base64 → 이미지 객체 변환
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))

        # ✅ 관상 분석용 프롬프트
        prompt = "이 사람의 얼굴을 관상학적으로 분석해줘. 성격, 재물운, 건강운을 한 문단씩 설명해줘. 명확하고 간결하게."

        # ✅ Gemini Vision API 호출
        response = model.generate_content(
            [prompt, image],
            generation_config={"temperature": 0.4}
        )

        result_text = response.text.strip()

        return jsonify({
            "generatedImgBase64": "",  # 아직은 그림 생성 안함
            "gwansangAnalysis": result_text
        })

    except Exception as e:
        import traceback
        print("에러 발생:", traceback.format_exc())
        return jsonify({"error": f"서버 내부 오류: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
