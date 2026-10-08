"""Service module 49940: business logic, no crypto."""


def calculate_total_49940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49940():
    return 'module 49940 handles orders and invoices'
