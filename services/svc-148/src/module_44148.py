"""Service module 44148: business logic, no crypto."""


def calculate_total_44148(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44148():
    return 'module 44148 handles orders and invoices'
