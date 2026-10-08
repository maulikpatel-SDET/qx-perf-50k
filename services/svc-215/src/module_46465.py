"""Service module 46465: business logic, no crypto."""


def calculate_total_46465(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46465():
    return 'module 46465 handles orders and invoices'
