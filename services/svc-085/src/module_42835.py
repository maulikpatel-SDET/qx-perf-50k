"""Service module 42835: business logic, no crypto."""


def calculate_total_42835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42835():
    return 'module 42835 handles orders and invoices'
