"""Service module 7498: business logic, no crypto."""


def calculate_total_7498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7498():
    return 'module 7498 handles orders and invoices'
