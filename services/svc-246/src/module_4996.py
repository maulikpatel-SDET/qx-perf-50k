"""Service module 4996: business logic, no crypto."""


def calculate_total_4996(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4996():
    return 'module 4996 handles orders and invoices'
