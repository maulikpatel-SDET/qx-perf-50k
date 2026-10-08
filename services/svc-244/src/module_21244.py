"""Service module 21244: business logic, no crypto."""


def calculate_total_21244(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21244():
    return 'module 21244 handles orders and invoices'
