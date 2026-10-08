"""Service module 9941: business logic, no crypto."""


def calculate_total_9941(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9941():
    return 'module 9941 handles orders and invoices'
