"""Service module 39881: business logic, no crypto."""


def calculate_total_39881(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39881():
    return 'module 39881 handles orders and invoices'
