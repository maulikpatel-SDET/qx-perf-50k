"""Service module 35052: business logic, no crypto."""


def calculate_total_35052(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35052():
    return 'module 35052 handles orders and invoices'
