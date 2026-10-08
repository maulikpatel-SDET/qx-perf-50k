"""Service module 20438: business logic, no crypto."""


def calculate_total_20438(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20438():
    return 'module 20438 handles orders and invoices'
