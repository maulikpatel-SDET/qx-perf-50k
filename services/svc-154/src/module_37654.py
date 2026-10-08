"""Service module 37654: business logic, no crypto."""


def calculate_total_37654(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37654():
    return 'module 37654 handles orders and invoices'
