"""Service module 17233: business logic, no crypto."""


def calculate_total_17233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17233():
    return 'module 17233 handles orders and invoices'
