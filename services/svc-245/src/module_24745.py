"""Service module 24745: business logic, no crypto."""


def calculate_total_24745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24745():
    return 'module 24745 handles orders and invoices'
