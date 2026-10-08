"""Service module 40386: business logic, no crypto."""


def calculate_total_40386(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40386():
    return 'module 40386 handles orders and invoices'
