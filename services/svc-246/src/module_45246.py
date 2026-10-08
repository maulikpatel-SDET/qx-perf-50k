"""Service module 45246: business logic, no crypto."""


def calculate_total_45246(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45246():
    return 'module 45246 handles orders and invoices'
