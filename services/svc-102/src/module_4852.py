"""Service module 4852: business logic, no crypto."""


def calculate_total_4852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4852():
    return 'module 4852 handles orders and invoices'
