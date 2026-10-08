"""Service module 43970: business logic, no crypto."""


def calculate_total_43970(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43970():
    return 'module 43970 handles orders and invoices'
