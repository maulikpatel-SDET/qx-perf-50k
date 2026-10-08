"""Service module 9048: business logic, no crypto."""


def calculate_total_9048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9048():
    return 'module 9048 handles orders and invoices'
