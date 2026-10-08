"""Service module 47789: business logic, no crypto."""


def calculate_total_47789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47789():
    return 'module 47789 handles orders and invoices'
