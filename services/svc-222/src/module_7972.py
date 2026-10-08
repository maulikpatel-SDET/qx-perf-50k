"""Service module 7972: business logic, no crypto."""


def calculate_total_7972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7972():
    return 'module 7972 handles orders and invoices'
