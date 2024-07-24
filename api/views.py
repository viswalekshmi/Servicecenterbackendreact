from rest_framework.response import Response

from api.models import Customer,Work

from api.serializers import CustomerSerializer,WorkSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework.decorators import action

from rest_framework import authentication,permissions


class CustomerListCreateView(ListAPIView, CreateAPIView):

    serializer_class = CustomerSerializer

    queryset = Customer.objects.all()

  


class CustomerRetrieveUpdateDestroyView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):

    serializer_class = CustomerSerializer

    queryset = Customer.objects.all()




class WorkCreateView(CreateAPIView):



    serializer_class=WorkSerializer

    queryset=Work.objects.all()


    def perform_create(self, serializer):

        id=self.kwargs.get("pk")

        instance=Customer.objects.get(id=id)

        serializer.save(customer_object=instance)



class WorkViewSet(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=WorkSerializer

    queryset=Work.objects.all()

  




