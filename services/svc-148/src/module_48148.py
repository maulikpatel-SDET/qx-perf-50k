"""Service module 48148: business logic, no crypto."""


def calculate_total_48148(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48148():
    return 'module 48148 handles orders and invoices'
