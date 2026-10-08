"""Service module 30352: business logic, no crypto."""


def calculate_total_30352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30352():
    return 'module 30352 handles orders and invoices'
