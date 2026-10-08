"""Service module 18010: business logic, no crypto."""


def calculate_total_18010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18010():
    return 'module 18010 handles orders and invoices'
