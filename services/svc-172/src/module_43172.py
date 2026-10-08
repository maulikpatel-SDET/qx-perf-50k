"""Service module 43172: business logic, no crypto."""


def calculate_total_43172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43172():
    return 'module 43172 handles orders and invoices'
