"""Service module 47645: business logic, no crypto."""


def calculate_total_47645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47645():
    return 'module 47645 handles orders and invoices'
