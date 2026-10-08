"""Service module 17209: business logic, no crypto."""


def calculate_total_17209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17209():
    return 'module 17209 handles orders and invoices'
