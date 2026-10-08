"""Service module 22826: business logic, no crypto."""


def calculate_total_22826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22826():
    return 'module 22826 handles orders and invoices'
