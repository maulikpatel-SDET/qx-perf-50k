"""Service module 4858: business logic, no crypto."""


def calculate_total_4858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4858():
    return 'module 4858 handles orders and invoices'
