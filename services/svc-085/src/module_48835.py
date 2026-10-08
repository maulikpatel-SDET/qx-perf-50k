"""Service module 48835: business logic, no crypto."""


def calculate_total_48835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48835():
    return 'module 48835 handles orders and invoices'
