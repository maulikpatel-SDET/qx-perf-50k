"""Service module 7903: business logic, no crypto."""


def calculate_total_7903(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7903():
    return 'module 7903 handles orders and invoices'
