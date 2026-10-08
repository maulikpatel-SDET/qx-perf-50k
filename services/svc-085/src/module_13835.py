"""Service module 13835: business logic, no crypto."""


def calculate_total_13835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13835():
    return 'module 13835 handles orders and invoices'
