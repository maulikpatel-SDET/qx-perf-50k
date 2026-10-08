"""Service module 29985: business logic, no crypto."""


def calculate_total_29985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29985():
    return 'module 29985 handles orders and invoices'
