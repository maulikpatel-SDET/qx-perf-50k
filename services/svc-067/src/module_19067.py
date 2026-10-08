"""Service module 19067: business logic, no crypto."""


def calculate_total_19067(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19067():
    return 'module 19067 handles orders and invoices'
