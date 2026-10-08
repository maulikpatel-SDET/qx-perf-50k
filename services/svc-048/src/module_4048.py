"""Service module 4048: business logic, no crypto."""


def calculate_total_4048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4048():
    return 'module 4048 handles orders and invoices'
