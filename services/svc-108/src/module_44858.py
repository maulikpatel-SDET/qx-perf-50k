"""Service module 44858: business logic, no crypto."""


def calculate_total_44858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44858():
    return 'module 44858 handles orders and invoices'
