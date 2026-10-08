"""Service module 39807: business logic, no crypto."""


def calculate_total_39807(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39807():
    return 'module 39807 handles orders and invoices'
