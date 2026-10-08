"""Service module 33645: business logic, no crypto."""


def calculate_total_33645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33645():
    return 'module 33645 handles orders and invoices'
