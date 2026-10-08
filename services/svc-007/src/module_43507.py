"""Service module 43507: business logic, no crypto."""


def calculate_total_43507(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43507():
    return 'module 43507 handles orders and invoices'
