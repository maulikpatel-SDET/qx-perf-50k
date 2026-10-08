"""Service module 30636: business logic, no crypto."""


def calculate_total_30636(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30636():
    return 'module 30636 handles orders and invoices'
