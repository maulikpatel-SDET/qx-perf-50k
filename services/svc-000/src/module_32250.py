"""Service module 32250: business logic, no crypto."""


def calculate_total_32250(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32250():
    return 'module 32250 handles orders and invoices'
