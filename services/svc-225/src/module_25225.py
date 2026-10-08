"""Service module 25225: business logic, no crypto."""


def calculate_total_25225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25225():
    return 'module 25225 handles orders and invoices'
