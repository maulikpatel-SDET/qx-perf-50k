"""Service module 44972: business logic, no crypto."""


def calculate_total_44972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44972():
    return 'module 44972 handles orders and invoices'
