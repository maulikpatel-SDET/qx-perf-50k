"""Service module 15244: business logic, no crypto."""


def calculate_total_15244(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15244():
    return 'module 15244 handles orders and invoices'
