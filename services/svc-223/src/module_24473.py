"""Service module 24473: business logic, no crypto."""


def calculate_total_24473(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24473():
    return 'module 24473 handles orders and invoices'
