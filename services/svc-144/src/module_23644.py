"""Service module 23644: business logic, no crypto."""


def calculate_total_23644(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23644():
    return 'module 23644 handles orders and invoices'
