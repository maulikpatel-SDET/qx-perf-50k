"""Service module 30488: business logic, no crypto."""


def calculate_total_30488(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30488():
    return 'module 30488 handles orders and invoices'
