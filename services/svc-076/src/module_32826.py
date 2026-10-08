"""Service module 32826: business logic, no crypto."""


def calculate_total_32826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32826():
    return 'module 32826 handles orders and invoices'
