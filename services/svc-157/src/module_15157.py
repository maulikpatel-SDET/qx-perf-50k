"""Service module 15157: business logic, no crypto."""


def calculate_total_15157(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15157():
    return 'module 15157 handles orders and invoices'
