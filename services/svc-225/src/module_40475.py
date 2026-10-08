"""Service module 40475: business logic, no crypto."""


def calculate_total_40475(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40475():
    return 'module 40475 handles orders and invoices'
