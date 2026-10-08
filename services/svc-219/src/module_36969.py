"""Service module 36969: business logic, no crypto."""


def calculate_total_36969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36969():
    return 'module 36969 handles orders and invoices'
