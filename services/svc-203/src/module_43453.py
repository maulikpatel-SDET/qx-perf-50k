"""Service module 43453: business logic, no crypto."""


def calculate_total_43453(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43453():
    return 'module 43453 handles orders and invoices'
