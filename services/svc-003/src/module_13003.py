"""Service module 13003: business logic, no crypto."""


def calculate_total_13003(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13003():
    return 'module 13003 handles orders and invoices'
