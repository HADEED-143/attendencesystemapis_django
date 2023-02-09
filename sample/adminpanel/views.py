from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . models import adminLogin, viewstudent, userreport, leaveapproval, attendencecount, gradingsys
from . serializers import loginadminSerializer, viewstuSerializer, reportSerializer, leaveSerializer, \
    attendenceSerializer, gradingSerializer


class adminlog(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            al = adminLogin.objects.get(id=id)
            serializer = loginadminSerializer(al)
            return Response(serializer.data)
        user = adminLogin.objects.all()
        serializer = loginadminSerializer(user, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = loginadminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        al = adminLogin.objects.get(pk=id)
        serializer = loginadminSerializer(al, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        al = adminLogin.objects.get(pk=id)
        serializers = loginadminSerializer(al, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'updated data'})
        return Response(serializers.errors)
    def delete(self, request, pk, format=None):
        id = pk
        al = adminLogin.objects.get(pk=id)
        al.delete()
        return Response({'msg':'Data deleted'})



class viewstud(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            vs = viewstudent.objects.get(id=id)
            serializer = viewstuSerializer(vs)
            return Response(serializer.data)
        vs = viewstudent.objects.all()
        serializer = viewstuSerializer(vs, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = viewstuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        vs = viewstudent.objects.get(pk=id)
        serializer = viewstuSerializer(vs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        vs = viewstudent.objects.get(pk=id)
        serializers = viewstuSerializer(vs, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'updated data'})
        return Response(serializers.errors)
    def delete(self, request, pk, format=None):
        id = pk
        vs = viewstudent.objects.get(pk=id)
        vs.delete()
        return Response({'msg':'Data deleted'})



class reportstu(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            rs = userreport.objects.get(id=id)
            serializer = reportSerializer(rs)
            return Response(serializer.data)
        rs = userreport.objects.all()
        serializer = reportSerializer(rs, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = reportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        rs = userreport.objects.get(pk=id)
        serializer = reportSerializer(rs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        rs = userreport.objects.get(pk=id)
        serializers = reportSerializer(rs, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'updated data'})
        return Response(serializers.errors)
    def delete(self, request, pk, format=None):
        id = pk
        rs = userreport.objects.get(pk=id)
        rs.delete()
        return Response({'msg':'Data deleted'})




class leaves(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            le = leaveapproval.objects.get(id=id)
            serializer = viewstuSerializer(le)
            return Response(serializer.data)
        vs = leaveapproval.objects.all()
        serializer = leaveSerializer(vs, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = leaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        le = leaveapproval.objects.get(pk=id)
        serializer = leaveSerializer(le, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        le = leaveapproval.objects.get(pk=id)
        serializers = leaveSerializer(le, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'updated data'})
        return Response(serializers.errors)
    def delete(self, request, pk, format=None):
        id = pk
        le = leaveapproval.objects.get(pk=id)
        le.delete()
        return Response({'msg':'Data deleted'})


class attenden(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            ac = attendencecount.objects.get(id=id)
            serializer = attendenceSerializer(ac)
            return Response(serializer.data)
        ac = attendencecount.objects.all()
        serializer = attendenceSerializer(ac, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = attendenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        ac = attendencecount.objects.get(pk=id)
        serializer = attendenceSerializer(ac, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        ac = attendencecount.objects.get(pk=id)
        serializers = attendenceSerializer(ac, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'updated data'})
        return Response(serializers.errors)
    def delete(self, request, pk, format=None):
        id = pk
        ac = attendencecount.objects.get(pk=id)
        ac.delete()
        return Response({'msg':'Data deleted'})


class grad(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            gr = gradingsys.objects.get(id=id)
            serializer = gradingSerializer(gr)
            return Response(serializer.data)
        gr = gradingsys.objects.all()
        serializer = gradingSerializer(gr, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = gradingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'created'}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        gr = gradingsys.objects.get(pk=id)
        serializer = gradingSerializer(gr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'complete update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        gr = gradingsys.objects.get(pk=id)
        serializers = gradingSerializer(gr, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg': 'updated data'})
        return Response(serializers.errors)

    def delete(self, request, pk, format=None):
        id = pk
        gr = gradingsys.objects.get(pk=id)
        gr.delete()
        return Response({'msg': 'Data deleted'})

    """
    def home(request):
   .objects.all()

    .objects.all()

         =Orders.count()

    delivered = .flter(status='').count()

    pending = .filter(status='').count()

    context = {}

    return render(request, 'Templates/dashboard.html', context)

def userpanel(request):

    .objects.all()
    return render(request, 'Templates/', {})

def adminpanel(request, pk_test):

    .objects.get(id=pk_test)

    .order_set.all()

    context = {}

    return render(request, 'Templates', context)
    """