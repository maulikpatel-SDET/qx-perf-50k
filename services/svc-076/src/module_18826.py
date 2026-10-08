"""Service module 18826: business logic, no crypto."""


def calculate_total_18826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18826():
    return 'module 18826 handles orders and invoices'
