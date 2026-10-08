"""Service module 15262: business logic, no crypto."""


def calculate_total_15262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15262():
    return 'module 15262 handles orders and invoices'
