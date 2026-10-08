"""Service module 25137: business logic, no crypto."""


def calculate_total_25137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25137():
    return 'module 25137 handles orders and invoices'
