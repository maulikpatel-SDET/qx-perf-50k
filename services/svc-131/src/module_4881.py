"""Service module 4881: business logic, no crypto."""


def calculate_total_4881(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4881():
    return 'module 4881 handles orders and invoices'
