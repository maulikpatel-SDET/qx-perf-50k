"""Service module 36013: business logic, no crypto."""


def calculate_total_36013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36013():
    return 'module 36013 handles orders and invoices'
