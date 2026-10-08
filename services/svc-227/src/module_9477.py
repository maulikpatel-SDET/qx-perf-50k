"""Service module 9477: business logic, no crypto."""


def calculate_total_9477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9477():
    return 'module 9477 handles orders and invoices'
