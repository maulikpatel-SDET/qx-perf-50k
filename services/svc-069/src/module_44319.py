"""Service module 44319: business logic, no crypto."""


def calculate_total_44319(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44319():
    return 'module 44319 handles orders and invoices'
