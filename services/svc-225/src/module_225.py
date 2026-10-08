"""Service module 225: business logic, no crypto."""


def calculate_total_225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_225():
    return 'module 225 handles orders and invoices'
