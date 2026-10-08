"""Service module 16347: business logic, no crypto."""


def calculate_total_16347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16347():
    return 'module 16347 handles orders and invoices'
