"""Service module 38225: business logic, no crypto."""


def calculate_total_38225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38225():
    return 'module 38225 handles orders and invoices'
