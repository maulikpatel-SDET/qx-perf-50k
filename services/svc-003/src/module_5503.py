"""Service module 5503: business logic, no crypto."""


def calculate_total_5503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5503():
    return 'module 5503 handles orders and invoices'
