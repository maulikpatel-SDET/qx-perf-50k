"""Service module 9210: business logic, no crypto."""


def calculate_total_9210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9210():
    return 'module 9210 handles orders and invoices'
