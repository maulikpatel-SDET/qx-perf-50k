"""Service module 11922: business logic, no crypto."""


def calculate_total_11922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11922():
    return 'module 11922 handles orders and invoices'
