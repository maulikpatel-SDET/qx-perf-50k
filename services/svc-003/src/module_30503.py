"""Service module 30503: business logic, no crypto."""


def calculate_total_30503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30503():
    return 'module 30503 handles orders and invoices'
