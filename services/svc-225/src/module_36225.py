"""Service module 36225: business logic, no crypto."""


def calculate_total_36225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36225():
    return 'module 36225 handles orders and invoices'
