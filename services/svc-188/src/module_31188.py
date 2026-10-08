"""Service module 31188: business logic, no crypto."""


def calculate_total_31188(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31188():
    return 'module 31188 handles orders and invoices'
