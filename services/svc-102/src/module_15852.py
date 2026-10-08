"""Service module 15852: business logic, no crypto."""


def calculate_total_15852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15852():
    return 'module 15852 handles orders and invoices'
