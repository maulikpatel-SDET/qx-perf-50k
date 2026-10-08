"""Service module 43697: business logic, no crypto."""


def calculate_total_43697(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43697():
    return 'module 43697 handles orders and invoices'
