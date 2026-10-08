"""Service module 24527: business logic, no crypto."""


def calculate_total_24527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24527():
    return 'module 24527 handles orders and invoices'
