"""Service module 41013: business logic, no crypto."""


def calculate_total_41013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41013():
    return 'module 41013 handles orders and invoices'
