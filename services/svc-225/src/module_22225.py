"""Service module 22225: business logic, no crypto."""


def calculate_total_22225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22225():
    return 'module 22225 handles orders and invoices'
