"""Service module 1539: business logic, no crypto."""


def calculate_total_1539(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1539():
    return 'module 1539 handles orders and invoices'
