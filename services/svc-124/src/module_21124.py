"""Service module 21124: business logic, no crypto."""


def calculate_total_21124(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21124():
    return 'module 21124 handles orders and invoices'
