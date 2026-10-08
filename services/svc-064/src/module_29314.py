"""Service module 29314: business logic, no crypto."""


def calculate_total_29314(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29314():
    return 'module 29314 handles orders and invoices'
