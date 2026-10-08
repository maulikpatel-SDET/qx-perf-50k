"""Service module 44243: business logic, no crypto."""


def calculate_total_44243(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44243():
    return 'module 44243 handles orders and invoices'
