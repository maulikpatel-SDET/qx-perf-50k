"""Service module 43234: business logic, no crypto."""


def calculate_total_43234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43234():
    return 'module 43234 handles orders and invoices'
