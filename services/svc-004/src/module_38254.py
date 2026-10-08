"""Service module 38254: business logic, no crypto."""


def calculate_total_38254(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38254():
    return 'module 38254 handles orders and invoices'
