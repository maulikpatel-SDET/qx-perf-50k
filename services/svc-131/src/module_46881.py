"""Service module 46881: business logic, no crypto."""


def calculate_total_46881(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46881():
    return 'module 46881 handles orders and invoices'
