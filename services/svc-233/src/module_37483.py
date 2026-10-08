"""Service module 37483: business logic, no crypto."""


def calculate_total_37483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37483():
    return 'module 37483 handles orders and invoices'
