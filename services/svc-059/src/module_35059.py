"""Service module 35059: business logic, no crypto."""


def calculate_total_35059(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35059():
    return 'module 35059 handles orders and invoices'
