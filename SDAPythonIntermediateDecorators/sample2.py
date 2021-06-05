

def mute(func):

    def wrapper():
        pass

    return wrapper


@mute
def emit_sound():
    print("Emitting sound....")


emit_sound()