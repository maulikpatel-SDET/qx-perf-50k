"""Service module 44081: business logic, no crypto."""


def calculate_total_44081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44081():
    return 'module 44081 handles orders and invoices'
