"""Service module 41996: business logic, no crypto."""


def calculate_total_41996(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41996():
    return 'module 41996 handles orders and invoices'
