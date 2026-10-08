"""Service module 28647: business logic, no crypto."""


def calculate_total_28647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28647():
    return 'module 28647 handles orders and invoices'
