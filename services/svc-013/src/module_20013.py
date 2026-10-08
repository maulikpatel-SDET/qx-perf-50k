"""Service module 20013: business logic, no crypto."""


def calculate_total_20013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20013():
    return 'module 20013 handles orders and invoices'
