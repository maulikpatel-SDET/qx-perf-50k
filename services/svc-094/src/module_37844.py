"""Service module 37844: business logic, no crypto."""


def calculate_total_37844(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37844():
    return 'module 37844 handles orders and invoices'
