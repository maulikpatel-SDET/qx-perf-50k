"""Service module 37982: business logic, no crypto."""


def calculate_total_37982(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37982():
    return 'module 37982 handles orders and invoices'
