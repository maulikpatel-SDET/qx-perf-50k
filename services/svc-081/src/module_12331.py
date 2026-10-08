"""Service module 12331: business logic, no crypto."""


def calculate_total_12331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12331():
    return 'module 12331 handles orders and invoices'
