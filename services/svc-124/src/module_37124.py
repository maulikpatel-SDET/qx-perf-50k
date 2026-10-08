"""Service module 37124: business logic, no crypto."""


def calculate_total_37124(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37124():
    return 'module 37124 handles orders and invoices'
