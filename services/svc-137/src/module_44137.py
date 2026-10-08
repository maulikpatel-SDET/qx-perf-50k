"""Service module 44137: business logic, no crypto."""


def calculate_total_44137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44137():
    return 'module 44137 handles orders and invoices'
