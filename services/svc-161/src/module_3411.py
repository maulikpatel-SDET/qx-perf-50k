"""Service module 3411: business logic, no crypto."""


def calculate_total_3411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3411():
    return 'module 3411 handles orders and invoices'
