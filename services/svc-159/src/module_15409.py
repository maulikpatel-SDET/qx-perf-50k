"""Service module 15409: business logic, no crypto."""


def calculate_total_15409(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15409():
    return 'module 15409 handles orders and invoices'
