"""Service module 40714: business logic, no crypto."""


def calculate_total_40714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40714():
    return 'module 40714 handles orders and invoices'
