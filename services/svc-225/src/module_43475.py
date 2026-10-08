"""Service module 43475: business logic, no crypto."""


def calculate_total_43475(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43475():
    return 'module 43475 handles orders and invoices'
