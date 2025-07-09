
import speech_recognition as sr
import pyttsx3
import cv2
import subprocess

engine = pyttsx3.init()
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def ouvir_microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Ouvindo...")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {texto}")
        return texto
    except:
        return ""

def ativar_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Câmera não encontrada")
        return
    ret, frame = cap.read()
    if ret:
        cv2.imshow("🧿 Oráculo te observa", frame)
        cv2.waitKey(3000)
    cap.release()
    cv2.destroyAllWindows()

def oraculo_loop():
    ativar_camera()
    falar("Estou aqui. O que deseja hoje?")
    comando = ouvir_microfone()
    if "proteger" in comando:
        falar("Montando defesa simbólica e legal.")
        subprocess.run(["echo", "Agente de proteção ativado"])
    elif "iniciar agentes" in comando:
        falar("Ativando exército agora.")
        subprocess.run(["echo", "Agentes n8n ativados"])
    else:
        falar("Comando não reconhecido.")

if __name__ == "__main__":
    oraculo_loop()
