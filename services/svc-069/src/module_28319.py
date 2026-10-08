"""Service module 28319: business logic, no crypto."""


def calculate_total_28319(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28319():
    return 'module 28319 handles orders and invoices'
