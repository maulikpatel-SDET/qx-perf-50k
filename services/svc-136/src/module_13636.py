"""Service module 13636: business logic, no crypto."""


def calculate_total_13636(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13636():
    return 'module 13636 handles orders and invoices'
