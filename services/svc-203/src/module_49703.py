"""Service module 49703: business logic, no crypto."""


def calculate_total_49703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49703():
    return 'module 49703 handles orders and invoices'
