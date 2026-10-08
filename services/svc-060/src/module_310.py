"""Service module 310: business logic, no crypto."""


def calculate_total_310(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_310():
    return 'module 310 handles orders and invoices'
