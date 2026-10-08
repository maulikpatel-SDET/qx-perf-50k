"""Service module 38940: business logic, no crypto."""


def calculate_total_38940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38940():
    return 'module 38940 handles orders and invoices'
