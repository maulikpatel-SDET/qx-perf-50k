"""Service module 42645: business logic, no crypto."""


def calculate_total_42645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42645():
    return 'module 42645 handles orders and invoices'
