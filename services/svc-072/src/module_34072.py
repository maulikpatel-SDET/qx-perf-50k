"""Service module 34072: business logic, no crypto."""


def calculate_total_34072(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34072():
    return 'module 34072 handles orders and invoices'
