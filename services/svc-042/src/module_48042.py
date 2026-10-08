"""Service module 48042: business logic, no crypto."""


def calculate_total_48042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48042():
    return 'module 48042 handles orders and invoices'
