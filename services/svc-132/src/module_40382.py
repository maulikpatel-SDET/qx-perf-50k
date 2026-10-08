"""Service module 40382: business logic, no crypto."""


def calculate_total_40382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40382():
    return 'module 40382 handles orders and invoices'
