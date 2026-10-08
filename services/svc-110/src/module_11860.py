"""Service module 11860: business logic, no crypto."""


def calculate_total_11860(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11860():
    return 'module 11860 handles orders and invoices'
