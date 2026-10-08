"""Service module 43426: business logic, no crypto."""


def calculate_total_43426(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43426():
    return 'module 43426 handles orders and invoices'
