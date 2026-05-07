from flask import Flask, render_template, request, jsonify
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

app = Flask(__name__)

# Supported Languages
languages = {

    "en": ("English", "🇺🇸"),
    "hi": ("Hindi", "🇮🇳"),
    "fr": ("French", "🇫🇷"),
    "es": ("Spanish", "🇪🇸"),
    "de": ("German", "🇩🇪"),
    "it": ("Italian", "🇮🇹"),
    "ja": ("Japanese", "🇯🇵"),
    "zh-cn": ("Chinese", "🇨🇳"),
    "ru": ("Russian", "🇷🇺"),
    "ko": ("Korean", "🇰🇷"),
    "ar": ("Arabic", "🇸🇦"),
    "pt": ("Portuguese", "🇵🇹"),
    "nl": ("Dutch", "🇳🇱"),
    "tr": ("Turkish", "🇹🇷"),
    "sv": ("Swedish", "🇸🇪"),
    "pl": ("Polish", "🇵🇱"),
    "da": ("Danish", "🇩🇰"),
    "fi": ("Finnish", "🇫🇮"),
    "no": ("Norwegian", "🇳🇴"),
    "uk": ("Ukrainian", "🇺🇦"),
    "el": ("Greek", "🇬🇷"),
    "th": ("Thai", "🇹🇭"),
    "vi": ("Vietnamese", "🇻🇳"),
    "id": ("Indonesian", "🇮🇩"),
    "ro": ("Romanian", "🇷🇴"),
    "hu": ("Hungarian", "🇭🇺"),
    "cs": ("Czech", "🇨🇿"),
    "sk": ("Slovak", "🇸🇰"),
    "hr": ("Croatian", "🇭🇷")
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_language():

    data = request.get_json()

    text = data.get('text', '').strip().lower()

    if not text:
        return jsonify({
            "language": "No Input",
            "flag": "❌",
            "code": "none"
        })

    # Massive Keyword Detection

    english_words = [
        "hello","hi","how are you","good morning","good evening",
        "thanks","thank you","welcome","friend","love","computer",
        "language","machine learning","artificial intelligence",
        "beautiful","weather","today","tomorrow","yes","no"
    ]

    french_words = [
        "bonjour","merci","salut","amour","fromage","paris",
        "comment allez-vous","bonne nuit","ami","français",
        "je t'aime","oui","non"
    ]

    spanish_words = [
        "hola","gracias","amigo","buenos días","buenas noches",
        "adios","mañana","sí","amor","español","como estas"
    ]

    german_words = [
        "hallo","danke","guten morgen","freund","liebe",
        "deutsch","tschüss","ja","nein","wie geht"
    ]

    italian_words = [
        "ciao","grazie","buongiorno","amico","amore",
        "italiano","roma","arrivederci","si"
    ]

    portuguese_words = [
        "olá","obrigado","bom dia","boa noite","amigo",
        "amor","português","sim","não"
    ]

    dutch_words = [
        "hallo","dank je","goedemorgen","vriend","liefde",
        "nederlands","ja","nee"
    ]

    turkish_words = [
        "merhaba","teşekkürler","günaydın","arkadaş",
        "aşk","evet","hayır","türkçe"
    ]

    swedish_words = [
        "hej","tack","god morgon","vän","kärlek",
        "svenska","ja","nej"
    ]

    polish_words = [
        "cześć","dziękuję","dzień dobry","przyjaciel",
        "miłość","tak","nie","polski"
    ]

    russian_words = [
        "привет","спасибо","доброе утро","друг",
        "любовь","да","нет","русский"
    ]

    arabic_words = [
        "مرحبا","شكرا","صباح الخير","صديق",
        "حب","نعم","لا","العربية"
    ]

    hindi_words = [
        "नमस्ते","दोस्त","धन्यवाद","सुप्रभात",
        "प्यार","हाँ","नहीं","हिंदी"
    ]

    japanese_words = [
        "こんにちは","ありがとう","おはよう",
        "友達","愛","はい","いいえ"
    ]

    chinese_words = [
        "你好","谢谢","早上好","朋友",
        "爱","是","不是"
    ]

    korean_words = [
        "안녕하세요","감사합니다","좋은 아침",
        "친구","사랑","네","아니요"
    ]

    # Detection Helper

    def contains(words):
        return any(word in text for word in words)

    # Manual Checks

    if contains(english_words):
        return jsonify({
            "language": "English",
            "flag": "🇺🇸",
            "code": "en"
        })

    elif contains(french_words):
        return jsonify({
            "language": "French",
            "flag": "🇫🇷",
            "code": "fr"
        })

    elif contains(spanish_words):
        return jsonify({
            "language": "Spanish",
            "flag": "🇪🇸",
            "code": "es"
        })

    elif contains(german_words):
        return jsonify({
            "language": "German",
            "flag": "🇩🇪",
            "code": "de"
        })

    elif contains(italian_words):
        return jsonify({
            "language": "Italian",
            "flag": "🇮🇹",
            "code": "it"
        })

    elif contains(portuguese_words):
        return jsonify({
            "language": "Portuguese",
            "flag": "🇵🇹",
            "code": "pt"
        })

    elif contains(dutch_words):
        return jsonify({
            "language": "Dutch",
            "flag": "🇳🇱",
            "code": "nl"
        })

    elif contains(turkish_words):
        return jsonify({
            "language": "Turkish",
            "flag": "🇹🇷",
            "code": "tr"
        })

    elif contains(swedish_words):
        return jsonify({
            "language": "Swedish",
            "flag": "🇸🇪",
            "code": "sv"
        })

    elif contains(polish_words):
        return jsonify({
            "language": "Polish",
            "flag": "🇵🇱",
            "code": "pl"
        })

    elif contains(russian_words):
        return jsonify({
            "language": "Russian",
            "flag": "🇷🇺",
            "code": "ru"
        })

    elif contains(arabic_words):
        return jsonify({
            "language": "Arabic",
            "flag": "🇸🇦",
            "code": "ar"
        })

    elif contains(hindi_words):
        return jsonify({
            "language": "Hindi",
            "flag": "🇮🇳",
            "code": "hi"
        })

    elif contains(japanese_words):
        return jsonify({
            "language": "Japanese",
            "flag": "🇯🇵",
            "code": "ja"
        })

    elif contains(chinese_words):
        return jsonify({
            "language": "Chinese",
            "flag": "🇨🇳",
            "code": "zh-cn"
        })

    elif contains(korean_words):
        return jsonify({
            "language": "Korean",
            "flag": "🇰🇷",
            "code": "ko"
        })

    # NLP Detection

    try:

        detected_code = detect(text)

        if detected_code in languages:

            language_name, flag = languages[detected_code]

        else:

            language_name = detected_code.upper()
            flag = "🌍"

        return jsonify({
            "language": language_name,
            "flag": flag,
            "code": detected_code
        })

    except Exception as e:

        print("Error:", e)

        return jsonify({
            "language": "Detection Failed",
            "flag": "❌",
            "code": "error"
        })

if __name__ == '__main__':
    app.run(debug=True)