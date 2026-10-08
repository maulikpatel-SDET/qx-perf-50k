"""Service module 45854: business logic, no crypto."""


def calculate_total_45854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45854():
    return 'module 45854 handles orders and invoices'
