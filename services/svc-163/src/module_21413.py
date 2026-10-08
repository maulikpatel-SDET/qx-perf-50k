"""Service module 21413: business logic, no crypto."""


def calculate_total_21413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21413():
    return 'module 21413 handles orders and invoices'
