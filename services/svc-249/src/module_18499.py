"""Service module 18499: business logic, no crypto."""


def calculate_total_18499(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18499():
    return 'module 18499 handles orders and invoices'
