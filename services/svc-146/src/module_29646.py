"""Service module 29646: business logic, no crypto."""


def calculate_total_29646(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29646():
    return 'module 29646 handles orders and invoices'
