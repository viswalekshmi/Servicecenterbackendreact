from rest_framework.response import Response

from api.models import Customer,Work

from api.serializers import CustomerSerializer,WorkSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework.decorators import action

from rest_framework import authentication,permissions

from rest_framework_simplejwt.authentication import JWTAuthentication




class CustomerListCreateView(ListAPIView, CreateAPIView):

    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = CustomerSerializer

    queryset = Customer.objects.all()

  


class CustomerRetrieveUpdateDestroyView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):

    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class = CustomerSerializer

    queryset = Customer.objects.all()




class WorkCreateView(CreateAPIView):


    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    serializer_class=WorkSerializer

    queryset=Work.objects.all()


    def perform_create(self, serializer):

        id=self.kwargs.get("pk")

        instance=Customer.objects.get(id=id)

        serializer.save(customer_object=instance)



class WorkViewSet(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=WorkSerializer

    queryset=Work.objects.all()

  




