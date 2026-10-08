"""Service module 49996: business logic, no crypto."""


def calculate_total_49996(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49996():
    return 'module 49996 handles orders and invoices'
