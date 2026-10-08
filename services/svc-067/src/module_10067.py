"""Service module 10067: business logic, no crypto."""


def calculate_total_10067(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10067():
    return 'module 10067 handles orders and invoices'
