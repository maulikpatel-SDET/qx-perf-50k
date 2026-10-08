"""Service module 23745: business logic, no crypto."""


def calculate_total_23745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23745():
    return 'module 23745 handles orders and invoices'
