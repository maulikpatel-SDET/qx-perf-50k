"""Service module 20499: business logic, no crypto."""


def calculate_total_20499(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20499():
    return 'module 20499 handles orders and invoices'
