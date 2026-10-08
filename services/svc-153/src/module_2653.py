"""Service module 2653: business logic, no crypto."""


def calculate_total_2653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2653():
    return 'module 2653 handles orders and invoices'
