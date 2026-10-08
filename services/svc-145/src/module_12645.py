"""Service module 12645: business logic, no crypto."""


def calculate_total_12645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12645():
    return 'module 12645 handles orders and invoices'
