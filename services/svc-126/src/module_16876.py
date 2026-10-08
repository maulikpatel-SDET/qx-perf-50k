"""Service module 16876: business logic, no crypto."""


def calculate_total_16876(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16876():
    return 'module 16876 handles orders and invoices'
