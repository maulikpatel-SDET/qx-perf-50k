"""Service module 41544: business logic, no crypto."""


def calculate_total_41544(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41544():
    return 'module 41544 handles orders and invoices'
