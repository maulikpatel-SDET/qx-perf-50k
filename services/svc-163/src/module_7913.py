"""Service module 7913: business logic, no crypto."""


def calculate_total_7913(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7913():
    return 'module 7913 handles orders and invoices'
