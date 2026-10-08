"""Service module 45903: business logic, no crypto."""


def calculate_total_45903(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45903():
    return 'module 45903 handles orders and invoices'
