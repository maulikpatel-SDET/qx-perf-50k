"""Service module 9636: business logic, no crypto."""


def calculate_total_9636(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9636():
    return 'module 9636 handles orders and invoices'
