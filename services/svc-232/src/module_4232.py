"""Service module 4232: business logic, no crypto."""


def calculate_total_4232(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4232():
    return 'module 4232 handles orders and invoices'
