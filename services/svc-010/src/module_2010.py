"""Service module 2010: business logic, no crypto."""


def calculate_total_2010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2010():
    return 'module 2010 handles orders and invoices'
