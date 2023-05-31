from django.db.models import Count, Sum as db_sum
from drf_yasg import openapi
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Employee, Department
from .serializers import BaseDepartmentSerializer, EmployeeDepAdminSerializer, DepartmentSerializer, \
    BaseEmployeeSerializer, DepartmentSerializerEmployeeSumPay, DepartmentEmployeeListSerializer


class CommonPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DepartmentApiSet(viewsets.ModelViewSet):
    """
        CRUD По всем Department
    """
    queryset = Department.objects.select_related('admin').all()
    serializer_class = BaseDepartmentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_object(self):
        if self.request.method == 'GET':
            self.serializer_class = DepartmentSerializer
        return super().get_object()

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.method == 'GET':
            self.serializer_class = DepartmentSerializer
            if not self.kwargs.get('pk'):
                query = Employee.objects.values('current_department').annotate(Count('pay')).annotate(db_sum('pay'))
                additional_data = dict(map(
                    lambda item: (item['current_department'], (item['pay__count'], item['pay__sum'])),
                    query))
                for item in qs:
                    if additional_data.get(item.pk):
                        setattr(item, 'employees', additional_data.get(item.pk)[0])
                        setattr(item, 'sum_pay', float(additional_data.get(item.pk)[1]))
                self.serializer_class = DepartmentSerializerEmployeeSumPay
        return qs

    @action(detail=True, methods=['get'])
    def by_department(self, request, pk=None):
        """
        сотрудники в депортаменте
        """
        obj = self.get_object()
        employee = Employee.objects.filter(current_department_id=obj.pk)
        setattr(obj, 'employees', list(employee))
        serializer = DepartmentEmployeeListSerializer(obj)
        return Response({**serializer.data})


class EmployeeApiSet(viewsets.ModelViewSet):
    """
        CRUD По всем Department
    """
    pagination_class = CommonPagination
    queryset = Employee.objects.select_related('current_department').all()
    serializer_class = BaseEmployeeSerializer
    permission_classes = (IsAuthenticated,)

    def get_filtering(self):
        flt = {}
        for key, val in self.request.query_params.items():
            if key.startswith('_') or key.startswith('__'):
                continue
            flt[key] = val
        return flt

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('last_name__icontains', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description='Filter: By last_name'),
            openapi.Parameter('current_department_id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description='Filter: By department')
        ])
    def list(self, *args, **kwargs):
        self.queryset = self.get_queryset().filter(**self.get_filtering())
        return super().list(*args, **kwargs)

    def get_object(self):
        if self.request.method == 'GET':
            self.serializer_class = EmployeeDepAdminSerializer
        return super().get_object()

    def get_queryset(self):
        if self.request.method == 'GET':
            self.serializer_class = EmployeeDepAdminSerializer
        return super().get_queryset()

