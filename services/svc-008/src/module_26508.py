"""Service module 26508: business logic, no crypto."""


def calculate_total_26508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26508():
    return 'module 26508 handles orders and invoices'
