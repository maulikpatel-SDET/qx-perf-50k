"""Service module 41243: business logic, no crypto."""


def calculate_total_41243(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41243():
    return 'module 41243 handles orders and invoices'
