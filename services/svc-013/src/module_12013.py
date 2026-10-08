"""Service module 12013: business logic, no crypto."""


def calculate_total_12013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12013():
    return 'module 12013 handles orders and invoices'
