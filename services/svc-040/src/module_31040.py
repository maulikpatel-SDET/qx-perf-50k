"""Service module 31040: business logic, no crypto."""


def calculate_total_31040(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31040():
    return 'module 31040 handles orders and invoices'
