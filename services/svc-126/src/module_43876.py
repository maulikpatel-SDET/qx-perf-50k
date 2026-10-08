"""Service module 43876: business logic, no crypto."""


def calculate_total_43876(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43876():
    return 'module 43876 handles orders and invoices'
