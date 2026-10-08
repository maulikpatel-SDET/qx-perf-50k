"""Service module 9739: business logic, no crypto."""


def calculate_total_9739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9739():
    return 'module 9739 handles orders and invoices'
