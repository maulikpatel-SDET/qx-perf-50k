"""Service module 43863: business logic, no crypto."""


def calculate_total_43863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43863():
    return 'module 43863 handles orders and invoices'
