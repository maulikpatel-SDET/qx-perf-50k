"""Service module 20196: business logic, no crypto."""


def calculate_total_20196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20196():
    return 'module 20196 handles orders and invoices'
