"""Service module 28863: business logic, no crypto."""


def calculate_total_28863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28863():
    return 'module 28863 handles orders and invoices'
