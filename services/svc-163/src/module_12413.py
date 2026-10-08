"""Service module 12413: business logic, no crypto."""


def calculate_total_12413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12413():
    return 'module 12413 handles orders and invoices'
