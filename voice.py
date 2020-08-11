import speech_recognition as sr


def listen(): 
    #criando o reconhecedor 
    rec = sr.Recognizer() 

    with sr.Microphone() as mic: #habilitando microfone e captando audio
        print("Olá, quero ouvir você")
        audio = rec.listen(mic) #ouvindo o que foi dito ao microfone

        try: 
            text = rec.recognize_google(audio,language='pt-BR')
            print(f'Eu entendi que você disse: {text}')
            
        except sr.UnknownValueError:
            print("Desculpe, não consegui entender o que você disse")

        except sr.RequestError as e:
            print(f'Erro ao chamar Google Speech Recognition: {e}')

        finally:
            print("Fale comigo mais uma vez!")


#chamando a função 
listen()

