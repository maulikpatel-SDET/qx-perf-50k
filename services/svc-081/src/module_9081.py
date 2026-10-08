"""Service module 9081: business logic, no crypto."""


def calculate_total_9081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9081():
    return 'module 9081 handles orders and invoices'
