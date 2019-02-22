from srCurriculos.models import Address

def create(country, state, city, street, resumeId):
    Address.objects.create(country=country,state=state,city=city,street=street,resume=resumeId)