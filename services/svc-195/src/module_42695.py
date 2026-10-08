"""Service module 42695: business logic, no crypto."""


def calculate_total_42695(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42695():
    return 'module 42695 handles orders and invoices'
