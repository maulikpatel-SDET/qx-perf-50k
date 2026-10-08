"""Service module 17521: business logic, no crypto."""


def calculate_total_17521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17521():
    return 'module 17521 handles orders and invoices'
