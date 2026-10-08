"""Service module 33023: business logic, no crypto."""


def calculate_total_33023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33023():
    return 'module 33023 handles orders and invoices'
