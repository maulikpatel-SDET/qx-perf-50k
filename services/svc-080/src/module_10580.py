"""Service module 10580: business logic, no crypto."""


def calculate_total_10580(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10580():
    return 'module 10580 handles orders and invoices'
