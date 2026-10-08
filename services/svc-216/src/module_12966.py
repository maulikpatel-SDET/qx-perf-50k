"""Service module 12966: business logic, no crypto."""


def calculate_total_12966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12966():
    return 'module 12966 handles orders and invoices'
