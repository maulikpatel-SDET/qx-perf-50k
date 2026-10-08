"""Service module 36645: business logic, no crypto."""


def calculate_total_36645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36645():
    return 'module 36645 handles orders and invoices'
