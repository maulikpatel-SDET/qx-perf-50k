"""Service module 34013: business logic, no crypto."""


def calculate_total_34013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34013():
    return 'module 34013 handles orders and invoices'
