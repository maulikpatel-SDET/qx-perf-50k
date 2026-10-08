"""Service module 22645: business logic, no crypto."""


def calculate_total_22645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22645():
    return 'module 22645 handles orders and invoices'
