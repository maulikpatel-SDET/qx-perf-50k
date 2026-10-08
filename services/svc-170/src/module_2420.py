"""Service module 2420: business logic, no crypto."""


def calculate_total_2420(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2420():
    return 'module 2420 handles orders and invoices'
