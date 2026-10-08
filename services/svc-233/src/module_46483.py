"""Service module 46483: business logic, no crypto."""


def calculate_total_46483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46483():
    return 'module 46483 handles orders and invoices'
