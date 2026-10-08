"""Service module 6763: business logic, no crypto."""


def calculate_total_6763(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6763():
    return 'module 6763 handles orders and invoices'
