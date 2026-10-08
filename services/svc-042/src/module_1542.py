"""Service module 1542: business logic, no crypto."""


def calculate_total_1542(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1542():
    return 'module 1542 handles orders and invoices'
