"""Service module 22903: business logic, no crypto."""


def calculate_total_22903(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22903():
    return 'module 22903 handles orders and invoices'
