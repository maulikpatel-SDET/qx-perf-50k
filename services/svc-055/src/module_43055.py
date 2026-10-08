"""Service module 43055: business logic, no crypto."""


def calculate_total_43055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43055():
    return 'module 43055 handles orders and invoices'
