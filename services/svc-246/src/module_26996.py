"""Service module 26996: business logic, no crypto."""


def calculate_total_26996(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26996():
    return 'module 26996 handles orders and invoices'
