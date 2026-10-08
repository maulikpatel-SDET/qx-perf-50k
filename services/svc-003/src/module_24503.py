"""Service module 24503: business logic, no crypto."""


def calculate_total_24503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24503():
    return 'module 24503 handles orders and invoices'
