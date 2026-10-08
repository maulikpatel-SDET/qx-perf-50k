"""Service module 19225: business logic, no crypto."""


def calculate_total_19225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19225():
    return 'module 19225 handles orders and invoices'
