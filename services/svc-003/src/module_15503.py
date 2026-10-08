"""Service module 15503: business logic, no crypto."""


def calculate_total_15503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15503():
    return 'module 15503 handles orders and invoices'
