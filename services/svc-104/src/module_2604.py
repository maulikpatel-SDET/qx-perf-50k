"""Service module 2604: business logic, no crypto."""


def calculate_total_2604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2604():
    return 'module 2604 handles orders and invoices'
