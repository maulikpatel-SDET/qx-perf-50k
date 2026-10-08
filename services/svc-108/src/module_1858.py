"""Service module 1858: business logic, no crypto."""


def calculate_total_1858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1858():
    return 'module 1858 handles orders and invoices'
