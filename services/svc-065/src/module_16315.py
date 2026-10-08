"""Service module 16315: business logic, no crypto."""


def calculate_total_16315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16315():
    return 'module 16315 handles orders and invoices'
