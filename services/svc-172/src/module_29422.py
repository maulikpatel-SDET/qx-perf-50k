"""Service module 29422: business logic, no crypto."""


def calculate_total_29422(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29422():
    return 'module 29422 handles orders and invoices'
