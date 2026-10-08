"""Service module 27244: business logic, no crypto."""


def calculate_total_27244(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27244():
    return 'module 27244 handles orders and invoices'
