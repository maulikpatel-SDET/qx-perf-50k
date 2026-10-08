"""Service module 49488: business logic, no crypto."""


def calculate_total_49488(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49488():
    return 'module 49488 handles orders and invoices'
