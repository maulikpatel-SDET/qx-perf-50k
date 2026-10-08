"""Service module 35745: business logic, no crypto."""


def calculate_total_35745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35745():
    return 'module 35745 handles orders and invoices'
