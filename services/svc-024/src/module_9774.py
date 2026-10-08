"""Service module 9774: business logic, no crypto."""


def calculate_total_9774(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9774():
    return 'module 9774 handles orders and invoices'
