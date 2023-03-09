from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Animal, Order
from .serializers import AnimalSerializer, OrderSerializer


# animals CRUD
@api_view(['GET'])
def get_animals(request):
    queryset = Animal.objects.all()
    serializer = AnimalSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_animal(request, **kwargs):
    pk = kwargs.get("pk", None)
    if not pk:
        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        queryset = Animal.objects.get(id=pk)
    except Animal.DoesNotExist:
        return Response({"error": f"Object {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AnimalSerializer(queryset)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_animal(request):
    serializer = AnimalSerializer(data=request.data)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT", "PATCH"])
def update_animal_info(request, **kwargs):
    pk = kwargs.get("pk", None)
    if not pk:
        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        queryset = Animal.objects.get(id=pk)
    except Animal.DoesNotExist:
        return Response({"error": f"Object {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AnimalSerializer(instance=queryset, data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_animal(request, **kwargs):
    pk = kwargs.get("pk", None)
    if not pk:
        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        queryset = Animal.objects.get(id=pk)
    except Animal.DoesNotExist:
        return Response({"error": f"Object {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    queryset.delete()

    return Response({"success": f"Object {pk} deleted successfully."}, status=status.HTTP_200_OK)


# Order CRUD
@api_view(['GET'])
def get_orders(request):
    queryset = Order.objects.all()
    serializer = OrderSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_order(request, **kwargs):
    pk = kwargs.get("pk", None)
    if not pk:
        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        queryset = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return Response({"error": f"Object {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(queryset)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_order(request):
    serializer = OrderSerializer(data=request.data)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT", "PATCH"])
def update_order_info(request, **kwargs):
    pk = kwargs.get("pk", None)
    if not pk:
        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        queryset = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return Response({"error": f"Object {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(instance=queryset, data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_order(request, **kwargs):
    pk = kwargs.get("pk", None)
    if not pk:
        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        queryset = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return Response({"error": f"Object {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    queryset.delete()

    return Response({"success": f"Object {pk} deleted successfully."}, status=status.HTTP_200_OK)
