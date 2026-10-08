"""Service module 36881: business logic, no crypto."""


def calculate_total_36881(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36881():
    return 'module 36881 handles orders and invoices'
