"""Service module 18472: business logic, no crypto."""


def calculate_total_18472(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18472():
    return 'module 18472 handles orders and invoices'
