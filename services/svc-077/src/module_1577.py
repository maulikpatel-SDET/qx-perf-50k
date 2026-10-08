"""Service module 1577: business logic, no crypto."""


def calculate_total_1577(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1577():
    return 'module 1577 handles orders and invoices'
