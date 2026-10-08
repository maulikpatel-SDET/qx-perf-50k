"""Service module 43399: business logic, no crypto."""


def calculate_total_43399(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43399():
    return 'module 43399 handles orders and invoices'
