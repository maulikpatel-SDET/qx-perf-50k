"""Service module 48826: business logic, no crypto."""


def calculate_total_48826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48826():
    return 'module 48826 handles orders and invoices'
