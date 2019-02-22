from srCurriculos.models import PastExperience

def createe(company, dtStart, dtEnd, description, resumeId):
    PastExperience.objects.create(
        company = company, 
        dt_start = dtStart, 
        dt_end = dtEnd, 
        description = description, 
        resume = resumeId
    )