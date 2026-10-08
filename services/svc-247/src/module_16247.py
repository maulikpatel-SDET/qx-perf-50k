"""Service module 16247: business logic, no crypto."""


def calculate_total_16247(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16247():
    return 'module 16247 handles orders and invoices'
