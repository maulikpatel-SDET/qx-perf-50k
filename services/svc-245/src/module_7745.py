"""Service module 7745: business logic, no crypto."""


def calculate_total_7745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7745():
    return 'module 7745 handles orders and invoices'
