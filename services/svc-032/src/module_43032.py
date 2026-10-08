"""Service module 43032: business logic, no crypto."""


def calculate_total_43032(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43032():
    return 'module 43032 handles orders and invoices'
