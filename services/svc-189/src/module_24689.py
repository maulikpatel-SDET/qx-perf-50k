"""Service module 24689: business logic, no crypto."""


def calculate_total_24689(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24689():
    return 'module 24689 handles orders and invoices'
