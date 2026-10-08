"""Service module 4557: business logic, no crypto."""


def calculate_total_4557(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4557():
    return 'module 4557 handles orders and invoices'
