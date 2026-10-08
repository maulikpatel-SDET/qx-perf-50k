"""Service module 24072: business logic, no crypto."""


def calculate_total_24072(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24072():
    return 'module 24072 handles orders and invoices'
