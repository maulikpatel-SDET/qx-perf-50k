"""Service module 39858: business logic, no crypto."""


def calculate_total_39858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39858():
    return 'module 39858 handles orders and invoices'
