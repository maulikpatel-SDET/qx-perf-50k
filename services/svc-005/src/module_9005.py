"""Service module 9005: business logic, no crypto."""


def calculate_total_9005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9005():
    return 'module 9005 handles orders and invoices'
