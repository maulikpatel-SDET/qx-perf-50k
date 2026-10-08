"""Service module 47806: business logic, no crypto."""


def calculate_total_47806(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47806():
    return 'module 47806 handles orders and invoices'
