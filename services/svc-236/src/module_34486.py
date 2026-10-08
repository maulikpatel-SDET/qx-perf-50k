"""Service module 34486: business logic, no crypto."""


def calculate_total_34486(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34486():
    return 'module 34486 handles orders and invoices'
