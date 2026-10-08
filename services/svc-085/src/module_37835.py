"""Service module 37835: business logic, no crypto."""


def calculate_total_37835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37835():
    return 'module 37835 handles orders and invoices'
