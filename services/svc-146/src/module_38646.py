"""Service module 38646: business logic, no crypto."""


def calculate_total_38646(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38646():
    return 'module 38646 handles orders and invoices'
