"""Service module 43626: business logic, no crypto."""


def calculate_total_43626(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43626():
    return 'module 43626 handles orders and invoices'
