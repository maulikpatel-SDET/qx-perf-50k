"""Service module 47072: business logic, no crypto."""


def calculate_total_47072(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47072():
    return 'module 47072 handles orders and invoices'
