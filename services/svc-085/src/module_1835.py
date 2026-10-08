"""Service module 1835: business logic, no crypto."""


def calculate_total_1835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1835():
    return 'module 1835 handles orders and invoices'
