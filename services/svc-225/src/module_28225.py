"""Service module 28225: business logic, no crypto."""


def calculate_total_28225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28225():
    return 'module 28225 handles orders and invoices'
