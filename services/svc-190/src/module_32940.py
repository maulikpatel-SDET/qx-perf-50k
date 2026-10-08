"""Service module 32940: business logic, no crypto."""


def calculate_total_32940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32940():
    return 'module 32940 handles orders and invoices'
