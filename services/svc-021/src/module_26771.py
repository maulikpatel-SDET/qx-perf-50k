"""Service module 26771: business logic, no crypto."""


def calculate_total_26771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26771():
    return 'module 26771 handles orders and invoices'
