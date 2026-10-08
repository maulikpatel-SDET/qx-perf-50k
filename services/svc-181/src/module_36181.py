"""Service module 36181: business logic, no crypto."""


def calculate_total_36181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36181():
    return 'module 36181 handles orders and invoices'
