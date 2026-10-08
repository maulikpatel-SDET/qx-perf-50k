"""Service module 28413: business logic, no crypto."""


def calculate_total_28413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28413():
    return 'module 28413 handles orders and invoices'
