import json
import traceback
from django.http import JsonResponse
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_condition import Or
from srcurriculos.resumes.models import Resume, Address, PastExperience
from rest_framework.views import APIView

class ResumesAPI(APIView):
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    
    def get(self, request):
        try:
            payload = request.GET
            if not payload:
                queryset = Resume.objects.all()
                response = json.dumps(list(queryset.values()))
                return JsonResponse({'response': response}, status = 200)

            if 'id' in payload:
                queryset = Resume.objects.filter(id=payload.get('id'))
                response = json.dumps(list(queryset.values()))
                return JsonResponse({'response': response}, status = 200)

            invalidKeys = []
            for key in payload:
                invalidKeys.append(key)
            
            raise ValueError('Keys: ' + ", ".join(invalidKeys) + ' are invalid')
        except ValueError as e:
            return JsonResponse({'response': str(e)}, status=400)

    def post(self, request):
        try:
            payload = request.data
            requiredKeys = {'first_name', 'last_name', 'age', 'email', 'desired_profession', 'phone_number'}
            if not all (key in payload for key in requiredKeys): # Validate obligatory parameters
                raise ValueError('Invalid request body')

            resumeSet = Resume.objects.create(
                first_name = payload['first_name'], 
                last_name = payload['last_name'], 
                age = payload['age'], 
                email = payload['email'], 
                desired_profession = payload['desired_profession'], 
                phone_number = payload['phone_number']
            )

            address = payload['address'] if 'address' in payload else []
            if address:
                Address.objects.create(
                    country = address['country'],
                    state = address['state'],
                    city = address['city'],
                    street = address['street'],
                    resume = resumeSet
                )
            
            pastExperiences = payload['past_experience'] if 'past_experience' in payload else []
            if pastExperiences and isinstance(pastExperiences, list):
                for experience in pastExperiences:
                    PastExperience.objects.create(
                        company = experience['company'], 
                        dt_start = experience['dt_start'], 
                        dt_end = experience['dt_end'], 
                        description = experience['description'], 
                        resume = resumeSet
                    )

            return JsonResponse({'status': 'sucess'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

    def delete(self, request):
        try:
            payload = json.loads(request.body)
            external_code_list = payload.get('external_code')
            if external_code_list:
                Resume.objects.filter(external_code__in=external_code_list).delete()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)