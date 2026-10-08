"""Service module 31984: business logic, no crypto."""


def calculate_total_31984(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31984():
    return 'module 31984 handles orders and invoices'
