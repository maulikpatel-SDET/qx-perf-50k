"""Service module 15835: business logic, no crypto."""


def calculate_total_15835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15835():
    return 'module 15835 handles orders and invoices'
