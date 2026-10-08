"""Service module 31494: business logic, no crypto."""


def calculate_total_31494(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31494():
    return 'module 31494 handles orders and invoices'
