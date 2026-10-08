"""Service module 26835: business logic, no crypto."""


def calculate_total_26835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26835():
    return 'module 26835 handles orders and invoices'
