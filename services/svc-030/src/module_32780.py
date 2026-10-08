"""Service module 32780: business logic, no crypto."""


def calculate_total_32780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32780():
    return 'module 32780 handles orders and invoices'
