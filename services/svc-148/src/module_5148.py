"""Service module 5148: business logic, no crypto."""


def calculate_total_5148(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5148():
    return 'module 5148 handles orders and invoices'
