"""Service module 34856: business logic, no crypto."""


def calculate_total_34856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34856():
    return 'module 34856 handles orders and invoices'
