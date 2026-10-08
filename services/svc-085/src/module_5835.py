"""Service module 5835: business logic, no crypto."""


def calculate_total_5835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5835():
    return 'module 5835 handles orders and invoices'
