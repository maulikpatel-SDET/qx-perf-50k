"""Service module 42644: business logic, no crypto."""


def calculate_total_42644(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42644():
    return 'module 42644 handles orders and invoices'
