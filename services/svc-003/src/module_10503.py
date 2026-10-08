"""Service module 10503: business logic, no crypto."""


def calculate_total_10503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10503():
    return 'module 10503 handles orders and invoices'
