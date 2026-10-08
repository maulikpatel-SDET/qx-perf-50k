"""Service module 20503: business logic, no crypto."""


def calculate_total_20503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20503():
    return 'module 20503 handles orders and invoices'
