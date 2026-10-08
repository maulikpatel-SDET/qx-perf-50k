"""Service module 9598: business logic, no crypto."""


def calculate_total_9598(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9598():
    return 'module 9598 handles orders and invoices'
