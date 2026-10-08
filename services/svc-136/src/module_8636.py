"""Service module 8636: business logic, no crypto."""


def calculate_total_8636(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8636():
    return 'module 8636 handles orders and invoices'
