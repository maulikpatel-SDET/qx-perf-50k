"""Service module 43336: business logic, no crypto."""


def calculate_total_43336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43336():
    return 'module 43336 handles orders and invoices'
