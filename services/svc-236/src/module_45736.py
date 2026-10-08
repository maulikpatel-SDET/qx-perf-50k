"""Service module 45736: business logic, no crypto."""


def calculate_total_45736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45736():
    return 'module 45736 handles orders and invoices'
