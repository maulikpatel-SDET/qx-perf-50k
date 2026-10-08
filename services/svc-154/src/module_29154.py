"""Service module 29154: business logic, no crypto."""


def calculate_total_29154(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29154():
    return 'module 29154 handles orders and invoices'
