"""Service module 4835: business logic, no crypto."""


def calculate_total_4835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4835():
    return 'module 4835 handles orders and invoices'
