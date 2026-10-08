"""Service module 21835: business logic, no crypto."""


def calculate_total_21835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21835():
    return 'module 21835 handles orders and invoices'
