"""Service module 22154: business logic, no crypto."""


def calculate_total_22154(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22154():
    return 'module 22154 handles orders and invoices'
