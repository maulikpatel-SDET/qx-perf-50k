"""Service module 3835: business logic, no crypto."""


def calculate_total_3835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3835():
    return 'module 3835 handles orders and invoices'
