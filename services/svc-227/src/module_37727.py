"""Service module 37727: business logic, no crypto."""


def calculate_total_37727(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37727():
    return 'module 37727 handles orders and invoices'
