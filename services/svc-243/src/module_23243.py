"""Service module 23243: business logic, no crypto."""


def calculate_total_23243(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23243():
    return 'module 23243 handles orders and invoices'
