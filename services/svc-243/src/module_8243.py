"""Service module 8243: business logic, no crypto."""


def calculate_total_8243(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8243():
    return 'module 8243 handles orders and invoices'
