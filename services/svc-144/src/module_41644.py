"""Service module 41644: business logic, no crypto."""


def calculate_total_41644(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41644():
    return 'module 41644 handles orders and invoices'
