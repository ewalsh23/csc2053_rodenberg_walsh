from django.shortcuts import render, HttpResponse
from translate import Translator

def home(request):
    if request.method == "POST":
        text = request.POST.get("translate")
        language = request.POST.get("language")
        
        if text and language:
            language_mapping = {
                'Arabic': 'ar',
                'Chinese': 'zh',
                'Dutch': 'nl',
                'German': 'de',
                'Greek': 'el',
                'Hindi': 'hi',
                'Italian': 'it',
                'Korean': 'ko',
                'Marathi': 'mr',
                'Polish': 'pl',
                'Russian': 'ru',
                'Spanish': 'es',
                'Thai': 'th',
                'Vietnamese': 'vi',
            }

            language_code = language_mapping.get(language)

            if language_code:
                try:
                    translator = Translator(to_lang=language_code)
                    translation = translator.translate(text)
                    return HttpResponse(translation)
                except Exception as e:
                    return HttpResponse(f"Error: {str(e)}")
            else:
                return HttpResponse("Error: Invalid language selected.")
        else:
            return HttpResponse("Error: Missing text or language.")
    
    return render(request, "main/index.html")