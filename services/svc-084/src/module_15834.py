"""Service module 15834: business logic, no crypto."""


def calculate_total_15834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15834():
    return 'module 15834 handles orders and invoices'
