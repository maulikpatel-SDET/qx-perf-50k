"""Service module 15996: business logic, no crypto."""


def calculate_total_15996(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15996():
    return 'module 15996 handles orders and invoices'
