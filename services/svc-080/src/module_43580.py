"""Service module 43580: business logic, no crypto."""


def calculate_total_43580(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43580():
    return 'module 43580 handles orders and invoices'
