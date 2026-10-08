"""Service module 37679: business logic, no crypto."""


def calculate_total_37679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37679():
    return 'module 37679 handles orders and invoices'
