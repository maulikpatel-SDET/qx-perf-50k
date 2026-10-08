"""Service module 8796: business logic, no crypto."""


def calculate_total_8796(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8796():
    return 'module 8796 handles orders and invoices'
