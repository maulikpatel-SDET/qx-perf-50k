"""Service module 12733: business logic, no crypto."""


def calculate_total_12733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12733():
    return 'module 12733 handles orders and invoices'
