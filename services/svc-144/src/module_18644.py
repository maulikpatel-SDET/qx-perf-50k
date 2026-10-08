"""Service module 18644: business logic, no crypto."""


def calculate_total_18644(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18644():
    return 'module 18644 handles orders and invoices'
