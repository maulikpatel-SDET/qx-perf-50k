"""Service module 48323: business logic, no crypto."""


def calculate_total_48323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48323():
    return 'module 48323 handles orders and invoices'
