"""Service module 44178: business logic, no crypto."""


def calculate_total_44178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44178():
    return 'module 44178 handles orders and invoices'
