"""Service module 2893: business logic, no crypto."""


def calculate_total_2893(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2893():
    return 'module 2893 handles orders and invoices'
