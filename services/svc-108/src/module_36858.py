"""Service module 36858: business logic, no crypto."""


def calculate_total_36858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36858():
    return 'module 36858 handles orders and invoices'
