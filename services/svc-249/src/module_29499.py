"""Service module 29499: business logic, no crypto."""


def calculate_total_29499(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29499():
    return 'module 29499 handles orders and invoices'
