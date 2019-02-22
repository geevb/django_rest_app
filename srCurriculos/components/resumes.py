import json
from srCurriculos.models import Resume
from srCurriculos.components.address import create
from srCurriculos.components.pastExperiences import createe

def get(resumeId = None):
    print(resumeId)
    resumes = Resume.objects.filter(id=resumeId) if id != None else Resume.objects.all()
    return json.dumps(list(resumes.values()))

def add(firstName, lastName, age, email, desiredProfession, phoneNumber, adress = [], pastExperiences = []):
    resume = Resume.objects.create(
        first_name = firstName, 
        last_name = lastName, 
        age = age, 
        email = email, 
        desired_profession = desiredProfession, 
        phone_number = phoneNumber
    )

    if adress:
        create(adress['country'], adress['state'], adress['city'], adress['street'], resume)

    if pastExperiences:
        if isinstance(pastExperiences, list):
            for experience in pastExperiences:
                createe(experience['company'], experience['dt_start'], experience['dt_end'], experience['description'], resume)
        else:
            createe(pastExperiences['company'], pastExperiences['dt_start'], pastExperiences['dt_end'], pastExperiences['description'], resume)
            
    return resume

        



