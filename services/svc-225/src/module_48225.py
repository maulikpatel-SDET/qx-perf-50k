"""Service module 48225: business logic, no crypto."""


def calculate_total_48225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48225():
    return 'module 48225 handles orders and invoices'
