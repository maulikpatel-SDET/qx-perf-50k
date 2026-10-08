"""Service module 43852: business logic, no crypto."""


def calculate_total_43852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43852():
    return 'module 43852 handles orders and invoices'
