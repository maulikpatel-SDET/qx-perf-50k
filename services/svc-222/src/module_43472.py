"""Service module 43472: business logic, no crypto."""


def calculate_total_43472(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43472():
    return 'module 43472 handles orders and invoices'
