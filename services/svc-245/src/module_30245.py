"""Service module 30245: business logic, no crypto."""


def calculate_total_30245(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30245():
    return 'module 30245 handles orders and invoices'
