"""Service module 49072: business logic, no crypto."""


def calculate_total_49072(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49072():
    return 'module 49072 handles orders and invoices'
