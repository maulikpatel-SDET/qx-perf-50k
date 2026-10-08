"""Service module 27124: business logic, no crypto."""


def calculate_total_27124(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27124():
    return 'module 27124 handles orders and invoices'
