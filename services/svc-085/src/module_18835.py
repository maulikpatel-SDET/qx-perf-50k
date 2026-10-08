"""Service module 18835: business logic, no crypto."""


def calculate_total_18835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18835():
    return 'module 18835 handles orders and invoices'
