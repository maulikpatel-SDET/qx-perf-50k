"""Service module 38826: business logic, no crypto."""


def calculate_total_38826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38826():
    return 'module 38826 handles orders and invoices'
