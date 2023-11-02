from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import SignUpserializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.contrib.auth.models import User
from base.models import Post
from base.serializer import PostSerializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def Routes(request):
    Route = [
         '/token',
         '/token/refresh',
         'register/',
         'CurrentUser/',
         'Posts_User/',
    ]
    return Response(Route)



@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpserializer(data=data)
    print(data)
    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                username = data['email'],
                password = make_password(data['password'])
            )
            return Response({'Details':'Account Created Successfully'},status=status.HTTP_201_CREATED)
        else : 
            return Response({'Error':'Account Already Exists'},status=status.HTTP_400_BAD_REQUEST)
    else : 
        return Response(user.errors)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentuser(request):
    user = UserSerializer(request.user)
    return Response(user.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_post_user(request):
    user = request.user
    posts = user.post_set.all()
    serializer = PostSerializer(posts,many=True)
    return Response({f"{user} Posts":serializer.data})


    




