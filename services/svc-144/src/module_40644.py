"""Service module 40644: business logic, no crypto."""


def calculate_total_40644(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40644():
    return 'module 40644 handles orders and invoices'
