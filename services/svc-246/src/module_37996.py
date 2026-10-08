"""Service module 37996: business logic, no crypto."""


def calculate_total_37996(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37996():
    return 'module 37996 handles orders and invoices'
