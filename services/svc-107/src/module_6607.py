"""Service module 6607: business logic, no crypto."""


def calculate_total_6607(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6607():
    return 'module 6607 handles orders and invoices'
