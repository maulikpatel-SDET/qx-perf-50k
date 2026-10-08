"""Service module 46118: business logic, no crypto."""


def calculate_total_46118(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46118():
    return 'module 46118 handles orders and invoices'
