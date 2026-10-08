"""Service module 43906: business logic, no crypto."""


def calculate_total_43906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43906():
    return 'module 43906 handles orders and invoices'
