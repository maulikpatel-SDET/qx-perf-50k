"""Service module 49745: business logic, no crypto."""


def calculate_total_49745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49745():
    return 'module 49745 handles orders and invoices'
