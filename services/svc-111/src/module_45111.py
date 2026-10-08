"""Service module 45111: business logic, no crypto."""


def calculate_total_45111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45111():
    return 'module 45111 handles orders and invoices'
