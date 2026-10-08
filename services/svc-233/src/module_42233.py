"""Service module 42233: business logic, no crypto."""


def calculate_total_42233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42233():
    return 'module 42233 handles orders and invoices'
