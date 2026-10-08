"""Service module 4415: business logic, no crypto."""


def calculate_total_4415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4415():
    return 'module 4415 handles orders and invoices'
