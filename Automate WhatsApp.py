import threading
import queue
import pywhatkit


def get_input(msg, chn):
    resp = input(msg + "\n")
    chn.put(resp)


def notfall_protokoll():
    phone_number = ""
    print("Initialisiere Notfallprotokoll...")
    pywhatkit.sendwhatmsg(phone_number, "Hey, ich wurde gerade entführt. Kannst du mich eventuell retten?",
                          time_hour=13, time_min=22)


def timeout_input(msg, timeout):
    chn = queue.Queue()
    thread = threading.Thread(target=get_input, args=(msg, chn))
    thread.daemon = True
    thread.start()
    try:
        resp = chn.get(True, timeout)
        return resp
    except queue.Empty:
        print("Nicht rechtzeitig geantwortet!")
        notfall_protokoll()
    return ""


if __name__ == "__main__":
    if "abcde" == timeout_input("Gib das Passwort ein:", 5):
        print("Richtig!")
    else:
        notfall_protokoll()
