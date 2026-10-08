"""Service module 43745: business logic, no crypto."""


def calculate_total_43745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43745():
    return 'module 43745 handles orders and invoices'
