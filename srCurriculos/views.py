import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from srCurriculos.models import Resume

class ResumesAPI(APIView):

    def get(self, request):
        try:
            payload = request.GET
            if not payload:
                return JsonResponse({'response': []}, status=200) # GET all resumes

            if 'id' in payload:                
                return JsonResponse({'response': []}, status=200) # GET specific resume

            invalidKeys = []
            for key in payload:
                invalidKeys.append(key)
            
            raise ValueError('Keys: ' + ", ".join(invalidKeys) + ' are invalid')
        except ValueError as e:
            return JsonResponse({'response': str(e)}, status=400)

    def post(self, request):    
        try:
            payload = request.POST
            return JsonResponse({'status': 'success'})
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