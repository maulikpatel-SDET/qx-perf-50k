"""Service module 10225: business logic, no crypto."""


def calculate_total_10225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10225():
    return 'module 10225 handles orders and invoices'
