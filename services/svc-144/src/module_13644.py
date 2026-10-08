"""Service module 13644: business logic, no crypto."""


def calculate_total_13644(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13644():
    return 'module 13644 handles orders and invoices'
