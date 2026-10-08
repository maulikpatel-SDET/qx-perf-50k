"""Service module 43842: business logic, no crypto."""


def calculate_total_43842(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43842():
    return 'module 43842 handles orders and invoices'
