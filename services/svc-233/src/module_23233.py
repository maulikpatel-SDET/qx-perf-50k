"""Service module 23233: business logic, no crypto."""


def calculate_total_23233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23233():
    return 'module 23233 handles orders and invoices'
