"""Service module 44351: business logic, no crypto."""


def calculate_total_44351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44351():
    return 'module 44351 handles orders and invoices'
