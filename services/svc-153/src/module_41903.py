"""Service module 41903: business logic, no crypto."""


def calculate_total_41903(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41903():
    return 'module 41903 handles orders and invoices'
