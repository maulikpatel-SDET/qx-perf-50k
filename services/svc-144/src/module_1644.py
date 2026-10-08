"""Service module 1644: business logic, no crypto."""


def calculate_total_1644(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1644():
    return 'module 1644 handles orders and invoices'
