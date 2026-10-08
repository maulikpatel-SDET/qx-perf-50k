"""Service module 40023: business logic, no crypto."""


def calculate_total_40023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40023():
    return 'module 40023 handles orders and invoices'
