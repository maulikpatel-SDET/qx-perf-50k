"""Service module 3996: business logic, no crypto."""


def calculate_total_3996(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3996():
    return 'module 3996 handles orders and invoices'
