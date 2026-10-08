"""Service module 17244: business logic, no crypto."""


def calculate_total_17244(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17244():
    return 'module 17244 handles orders and invoices'
