"""Service module 15413: business logic, no crypto."""


def calculate_total_15413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15413():
    return 'module 15413 handles orders and invoices'
