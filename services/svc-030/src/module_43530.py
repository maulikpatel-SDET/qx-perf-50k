"""Service module 43530: business logic, no crypto."""


def calculate_total_43530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43530():
    return 'module 43530 handles orders and invoices'
