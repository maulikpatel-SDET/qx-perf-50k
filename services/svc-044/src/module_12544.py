"""Service module 12544: business logic, no crypto."""


def calculate_total_12544(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12544():
    return 'module 12544 handles orders and invoices'
