"""Service module 24645: business logic, no crypto."""


def calculate_total_24645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24645():
    return 'module 24645 handles orders and invoices'
