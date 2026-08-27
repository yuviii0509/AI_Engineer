resume_memory = {}


def save_resume(data):
    global resume_memory
    resume_memory = data


def get_resume():
    return resume_memory