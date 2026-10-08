"""Service module 43014: business logic, no crypto."""


def calculate_total_43014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43014():
    return 'module 43014 handles orders and invoices'
