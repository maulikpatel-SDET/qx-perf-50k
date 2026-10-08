"""Service module 38745: business logic, no crypto."""


def calculate_total_38745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38745():
    return 'module 38745 handles orders and invoices'
