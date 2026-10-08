"""Service module 31225: business logic, no crypto."""


def calculate_total_31225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31225():
    return 'module 31225 handles orders and invoices'
