"""Service module 26323: business logic, no crypto."""


def calculate_total_26323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26323():
    return 'module 26323 handles orders and invoices'
