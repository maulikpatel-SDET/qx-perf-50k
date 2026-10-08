"""Service module 43746: business logic, no crypto."""


def calculate_total_43746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43746():
    return 'module 43746 handles orders and invoices'
