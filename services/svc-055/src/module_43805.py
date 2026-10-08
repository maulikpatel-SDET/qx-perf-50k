"""Service module 43805: business logic, no crypto."""


def calculate_total_43805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43805():
    return 'module 43805 handles orders and invoices'
