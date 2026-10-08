"""Service module 31244: business logic, no crypto."""


def calculate_total_31244(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31244():
    return 'module 31244 handles orders and invoices'
