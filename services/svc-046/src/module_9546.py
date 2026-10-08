"""Service module 9546: business logic, no crypto."""


def calculate_total_9546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9546():
    return 'module 9546 handles orders and invoices'
