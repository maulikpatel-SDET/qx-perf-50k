"""Service module 17232: business logic, no crypto."""


def calculate_total_17232(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17232():
    return 'module 17232 handles orders and invoices'
