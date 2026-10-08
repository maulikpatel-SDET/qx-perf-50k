"""Service module 42940: business logic, no crypto."""


def calculate_total_42940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42940():
    return 'module 42940 handles orders and invoices'
