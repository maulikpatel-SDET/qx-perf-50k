"""Service module 37278: business logic, no crypto."""


def calculate_total_37278(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37278():
    return 'module 37278 handles orders and invoices'
