"""Service module 27852: business logic, no crypto."""


def calculate_total_27852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27852():
    return 'module 27852 handles orders and invoices'
