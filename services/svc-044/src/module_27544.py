"""Service module 27544: business logic, no crypto."""


def calculate_total_27544(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27544():
    return 'module 27544 handles orders and invoices'
