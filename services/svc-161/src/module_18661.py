"""Service module 18661: business logic, no crypto."""


def calculate_total_18661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18661():
    return 'module 18661 handles orders and invoices'
