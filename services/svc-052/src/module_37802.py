"""Service module 37802: business logic, no crypto."""


def calculate_total_37802(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37802():
    return 'module 37802 handles orders and invoices'
