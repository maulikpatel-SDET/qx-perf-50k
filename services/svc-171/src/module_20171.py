"""Service module 20171: business logic, no crypto."""


def calculate_total_20171(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20171():
    return 'module 20171 handles orders and invoices'
