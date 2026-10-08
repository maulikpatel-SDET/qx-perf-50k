"""Service module 25204: business logic, no crypto."""


def calculate_total_25204(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25204():
    return 'module 25204 handles orders and invoices'
