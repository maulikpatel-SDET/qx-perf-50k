"""Service module 14181: business logic, no crypto."""


def calculate_total_14181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14181():
    return 'module 14181 handles orders and invoices'
