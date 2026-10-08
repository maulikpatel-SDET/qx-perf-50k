"""Service module 6636: business logic, no crypto."""


def calculate_total_6636(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6636():
    return 'module 6636 handles orders and invoices'
