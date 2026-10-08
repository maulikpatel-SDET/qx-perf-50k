"""Service module 43125: business logic, no crypto."""


def calculate_total_43125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43125():
    return 'module 43125 handles orders and invoices'
