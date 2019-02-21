from srCurriculos.models import Resume

def get(id=None):
    return Resume.objects.find(id=id) if id != None else Resume.objects.find()