"""Service module 20042: business logic, no crypto."""


def calculate_total_20042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20042():
    return 'module 20042 handles orders and invoices'
