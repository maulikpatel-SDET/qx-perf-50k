"""Service module 12826: business logic, no crypto."""


def calculate_total_12826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12826():
    return 'module 12826 handles orders and invoices'
