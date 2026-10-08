"""Service module 1003: business logic, no crypto."""


def calculate_total_1003(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1003():
    return 'module 1003 handles orders and invoices'
