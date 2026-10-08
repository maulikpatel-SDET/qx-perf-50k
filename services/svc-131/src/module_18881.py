"""Service module 18881: business logic, no crypto."""


def calculate_total_18881(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18881():
    return 'module 18881 handles orders and invoices'
