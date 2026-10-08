"""Service module 43508: business logic, no crypto."""


def calculate_total_43508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43508():
    return 'module 43508 handles orders and invoices'
