"""Service module 25003: business logic, no crypto."""


def calculate_total_25003(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25003():
    return 'module 25003 handles orders and invoices'
