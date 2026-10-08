"""Service module 38539: business logic, no crypto."""


def calculate_total_38539(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38539():
    return 'module 38539 handles orders and invoices'
