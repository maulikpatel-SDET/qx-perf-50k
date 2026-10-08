"""Service module 2247: business logic, no crypto."""


def calculate_total_2247(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2247():
    return 'module 2247 handles orders and invoices'
