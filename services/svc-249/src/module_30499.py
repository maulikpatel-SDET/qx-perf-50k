"""Service module 30499: business logic, no crypto."""


def calculate_total_30499(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30499():
    return 'module 30499 handles orders and invoices'
