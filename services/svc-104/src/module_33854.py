"""Service module 33854: business logic, no crypto."""


def calculate_total_33854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33854():
    return 'module 33854 handles orders and invoices'
