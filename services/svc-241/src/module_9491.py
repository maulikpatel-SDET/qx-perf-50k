"""Service module 9491: business logic, no crypto."""


def calculate_total_9491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9491():
    return 'module 9491 handles orders and invoices'
