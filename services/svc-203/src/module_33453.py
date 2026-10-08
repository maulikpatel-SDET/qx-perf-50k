"""Service module 33453: business logic, no crypto."""


def calculate_total_33453(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33453():
    return 'module 33453 handles orders and invoices'
