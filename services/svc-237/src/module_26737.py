"""Service module 26737: business logic, no crypto."""


def calculate_total_26737(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26737():
    return 'module 26737 handles orders and invoices'
