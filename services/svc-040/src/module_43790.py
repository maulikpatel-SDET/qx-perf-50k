"""Service module 43790: business logic, no crypto."""


def calculate_total_43790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43790():
    return 'module 43790 handles orders and invoices'
