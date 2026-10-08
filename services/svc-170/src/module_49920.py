"""Service module 49920: business logic, no crypto."""


def calculate_total_49920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49920():
    return 'module 49920 handles orders and invoices'
