"""Service module 44125: business logic, no crypto."""


def calculate_total_44125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44125():
    return 'module 44125 handles orders and invoices'
