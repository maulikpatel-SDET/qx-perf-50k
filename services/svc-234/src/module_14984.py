"""Service module 14984: business logic, no crypto."""


def calculate_total_14984(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14984():
    return 'module 14984 handles orders and invoices'
