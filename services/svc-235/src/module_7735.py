"""Service module 7735: business logic, no crypto."""


def calculate_total_7735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7735():
    return 'module 7735 handles orders and invoices'
