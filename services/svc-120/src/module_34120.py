"""Service module 34120: business logic, no crypto."""


def calculate_total_34120(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34120():
    return 'module 34120 handles orders and invoices'
