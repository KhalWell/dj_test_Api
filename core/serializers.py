from rest_framework import serializers
from .models import Job, Employee, Department


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class BaseEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeToDepartmentSerializer(BaseEmployeeSerializer):
    #  Предпологаем, что поле id это что-то вроде табельного номера сотрудника, и только он может быть уникальным
    #  Конечно можно сделать unique together по ФИО, но ведь бывают полные тески ...
    #  В DepartmentSerializer закоментированна реализация
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'father_name',)


class BaseDepartmentSerializer(serializers.ModelSerializer):
    # admin = EmployeeToDepartmentSerializer(many=False)

    class Meta:
        model = Department
        fields = "__all__"

    # def update(self, instance, validated_data):
    #     admin = validated_data.pop("admin")
    #     employee = Employee.objects.get(first_name=admin['first_name'],
    #                                     last_name=admin['last_name'],
    #                                     father_name=admin['father_name']
    #                                     )
    #     instance.admin = employee
    #     return instance
    #
    # def create(self, validated_data):
    #     admin = validated_data.pop("admin")
    #     employee = Employee.objects.get(first_name=admin['first_name'],
    #                                     last_name=admin['last_name'],
    #                                     father_name=admin['father_name']
    #                                     )
    #     instance = super().create(validated_data)
    #     instance.admin = employee
    #     return instance


class DepartmentSerializer(BaseDepartmentSerializer):
    admin = EmployeeToDepartmentSerializer(many=False)


class DepartmentEmployeeListSerializer(DepartmentSerializer):
    employees = serializers.ListField(child=BaseEmployeeSerializer())


class DepartmentSerializerEmployeeSumPay(DepartmentSerializer):
    employees = serializers.IntegerField()
    sum_pay = serializers.FloatField()


class EmployeeSerializer(BaseEmployeeSerializer):
    current_department = BaseDepartmentSerializer(many=False)


class EmployeeDepAdminSerializer(BaseEmployeeSerializer):
    current_department = DepartmentSerializer(many=False)
