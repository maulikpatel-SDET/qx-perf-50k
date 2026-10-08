"""Service module 10182: business logic, no crypto."""


def calculate_total_10182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10182():
    return 'module 10182 handles orders and invoices'
