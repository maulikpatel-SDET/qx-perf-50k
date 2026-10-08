"""Service module 9653: business logic, no crypto."""


def calculate_total_9653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9653():
    return 'module 9653 handles orders and invoices'
