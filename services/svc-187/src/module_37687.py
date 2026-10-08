"""Service module 37687: business logic, no crypto."""


def calculate_total_37687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37687():
    return 'module 37687 handles orders and invoices'
