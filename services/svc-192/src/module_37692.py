"""Service module 37692: business logic, no crypto."""


def calculate_total_37692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37692():
    return 'module 37692 handles orders and invoices'
