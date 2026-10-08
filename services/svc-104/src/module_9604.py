"""Service module 9604: business logic, no crypto."""


def calculate_total_9604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9604():
    return 'module 9604 handles orders and invoices'
