"""Service module 22233: business logic, no crypto."""


def calculate_total_22233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22233():
    return 'module 22233 handles orders and invoices'
