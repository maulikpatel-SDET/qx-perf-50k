"""Service module 37745: business logic, no crypto."""


def calculate_total_37745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37745():
    return 'module 37745 handles orders and invoices'
