"""Service module 21985: business logic, no crypto."""


def calculate_total_21985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21985():
    return 'module 21985 handles orders and invoices'
