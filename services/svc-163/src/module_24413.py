"""Service module 24413: business logic, no crypto."""


def calculate_total_24413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24413():
    return 'module 24413 handles orders and invoices'
