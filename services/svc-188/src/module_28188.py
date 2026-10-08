"""Service module 28188: business logic, no crypto."""


def calculate_total_28188(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28188():
    return 'module 28188 handles orders and invoices'
