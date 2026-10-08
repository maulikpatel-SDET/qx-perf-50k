"""Service module 42398: business logic, no crypto."""


def calculate_total_42398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42398():
    return 'module 42398 handles orders and invoices'
