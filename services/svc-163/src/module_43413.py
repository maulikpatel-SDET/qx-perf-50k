"""Service module 43413: business logic, no crypto."""


def calculate_total_43413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43413():
    return 'module 43413 handles orders and invoices'
