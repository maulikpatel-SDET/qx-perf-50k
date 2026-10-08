"""Service module 30826: business logic, no crypto."""


def calculate_total_30826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30826():
    return 'module 30826 handles orders and invoices'
