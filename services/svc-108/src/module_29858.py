"""Service module 29858: business logic, no crypto."""


def calculate_total_29858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29858():
    return 'module 29858 handles orders and invoices'
