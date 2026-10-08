"""Service module 3013: business logic, no crypto."""


def calculate_total_3013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3013():
    return 'module 3013 handles orders and invoices'
