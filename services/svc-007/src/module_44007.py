"""Service module 44007: business logic, no crypto."""


def calculate_total_44007(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44007():
    return 'module 44007 handles orders and invoices'
