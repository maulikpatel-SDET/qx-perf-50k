"""Service module 7284: business logic, no crypto."""


def calculate_total_7284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7284():
    return 'module 7284 handles orders and invoices'
