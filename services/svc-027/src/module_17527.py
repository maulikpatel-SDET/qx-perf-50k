"""Service module 17527: business logic, no crypto."""


def calculate_total_17527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17527():
    return 'module 17527 handles orders and invoices'
