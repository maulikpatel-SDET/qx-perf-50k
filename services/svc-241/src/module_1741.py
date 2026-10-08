"""Service module 1741: business logic, no crypto."""


def calculate_total_1741(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1741():
    return 'module 1741 handles orders and invoices'
