"""Service module 43134: business logic, no crypto."""


def calculate_total_43134(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43134():
    return 'module 43134 handles orders and invoices'
