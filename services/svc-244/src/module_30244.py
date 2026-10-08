"""Service module 30244: business logic, no crypto."""


def calculate_total_30244(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30244():
    return 'module 30244 handles orders and invoices'
