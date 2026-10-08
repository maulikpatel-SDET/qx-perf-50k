"""Service module 10148: business logic, no crypto."""


def calculate_total_10148(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10148():
    return 'module 10148 handles orders and invoices'
